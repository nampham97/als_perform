import json
import pandas as pd
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
from os import environ

import json
from datetime import datetime

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
def ghi_file_log(data="", type_write="a", path="log_temp.txt", type_file="txt"):
    with open(f"logs/{path}.{type_file}", type_write) as file:
        # Ghi dữ liệu vào file
        file.write(data)


def get_config():
    load_dotenv()
    hostname = environ.get("BPM_REST_HOSTNAME")
    username = environ.get("BPM_REST_USERNAME")
    password = environ.get("BPM_REST_PASSWORD")

    return hostname, username, password


def read_file(har_file_path):
    with open(har_file_path, "r", encoding="utf-8") as file:
        har_data = json.load(file)

    # Extract the entries from the HAR data
    entries = har_data.get("log", {}).get("entries", [])

    # Check the structure and a few sample entries
    sample_entries = entries[:5]

    len(entries), sample_entries
    return entries


def write_export_file(data, fileName="example.xlsx"):
    with pd.ExcelWriter(f"exports/{fileName}") as writer:
        # Write each DataFrame to a different sheet
        data[0].to_excel(writer, sheet_name="Timings", index=False)
        data[1].to_excel(writer, sheet_name="Slow Requests", index=False)
        data[2].to_excel(writer, sheet_name="Service Breakdown")


def extract_service_and_note(url):
    # Phân tích URL thành các thành phần
    parsed_url = urlparse(url)
    # Trích xuất giá trị
    type_name = parsed_url.path.split("/")[1]
    service_type = parsed_url.path.split("/")[-2]
    service_id = parsed_url.path.split("/")[-1]
    note = parsed_url.query.split("&")[-1].split("=")[-1]
    name_service = "Không có ServiceName"
    if service_type == "service":
        name_service, note = handle_detail(service_id)

    return type_name, service_type, name_service, note


def create_dataFrame_json(entries):
    timing_data = []

    for entry in entries:
        request_url = entry["request"]["url"]
        request_method = entry["request"]["method"]
        response_status = entry["response"]["status"]
        timings = entry["timings"]

        timing_data.append(
            {
                "url": request_url,
                "method": request_method,
                "status": response_status,
                "blocked": timings.get("blocked", 0),
                "dns": timings.get("dns", 0),
                "connect": timings.get("connect", 0),
                "ssl": timings.get("ssl", 0),
                "send": timings.get("send", 0),
                "wait": timings.get("wait", 0),
                "receive": timings.get("receive", 0),
                "total_time": entry.get("time", 0),
            }
        )

    return timing_data


def modify_column_df(
    df_timings: pd.DataFrame, path_report="exports/timing.xlsx"
) -> pd.DataFrame:

    (
        df_timings["Loại Req"],
        df_timings["Loại Service"],
        # df_timings["service_id"],
        df_timings["service_name_in_bpm"],
        df_timings["note"],
    ) = zip(*df_timings["url"].apply(extract_service_and_note))

    columns_to_sum = [
        "blocked",
        "dns",
        "connect",
        "ssl",
        "send",
        "wait",
        "receive",
        "total_time",
    ]
    df_sum = df_timings[columns_to_sum].sum()
    df_sum.name = "Tổng cộng"
    df_timings = pd.concat([df_timings, df_sum.to_frame().T], ignore_index=True)
    df_timings.loc[df_timings.index[-1], "url"] = "Tổng cộng"
    df_timings.to_excel(f"exports/{path_report}")

    # return df_timings


def check_properties(properties):
    result = {
        'is_loop_code' : False,
        'is_have_los_bo' : False
    }
    if properties is None:
        return result

    for prop_name, prop_value in properties.items():
        if prop_name.lower() in [
            "run",
            "count",
            "loop",
            "run1",
            "count1",
            "loop1",
            "length",
        ]:
            result['is_loop_code'] = True
        if prop_value['type'] == 'LOS_PROCESS':
            result['is_have_los_bo'] = True
            
    return result


def create_call_api(path_api, params):
    hostname, username, password = get_config()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    url = f"https://{hostname}/rest/bpm/wle/v1/{path_api}"
    auth = (username, password)

    response = requests.get(
        url, auth=auth, verify=False, params=params, headers=headers
    )

    if response.status_code == 200:
        return response.json()

    return {"status": response.status_code, "message": "Error API"}


def handle_detail(service_id):
    URL_GET_SERVICE = f"serviceModel/{service_id}"
    URL_GET_SERVICE_DETAIL = f"visual/serviceModel/{service_id}"
    response = create_call_api(URL_GET_SERVICE, {"parts": "all"})

    if response["status"] == "200":
        data = response["data"]
        data_header = data["header"]
        data_diagram = data["diagram"]
        data_dataModel = data["dataModel"]

        name_service = data_header["name"]
        snapshotId_of_service = data_header["snapshotId"]
        note = ""
        # duyet list dataModel tim bien co ten la count, run, loop, run1, count1, loop1, length,
        check_prop = check_properties(data_dataModel["properties"])
        if check_prop['is_loop_code']:
            note += "This might be a loop service in BPM\n"
        if check_prop['is_have_los_bo']:
            note += "Have BO LOS_PROCESS\n"
        # end duyet prop loop

        # kiem tra co sub process k
        # https://10.53.252.201:9443/rest/bpm/wle/v1/visual/serviceModel/1.35db8ef7-7cc0-4e95-b98f-a854ae823627?snapshotId=2064.483db852-65e9-42b7-bef6-acd9d342053a
        # kiem tra neu item > serviceType:"Integration Service" la DB
        # neu 	"SCA Service" la tich hop
        # neu Service Flow thi chay tiep 2 cai tren - tam thoi chua lam vi de quy

        response_detail = create_call_api(
            URL_GET_SERVICE_DETAIL, {"snapshotId": snapshotId_of_service}
        )

        if response_detail["status"] == "200":
            data_detail = response_detail["data"]["items"]
            for item in data_detail:
                if item.get("serviceType") == "Integration Service":
                    note += f"This might be a Database call Store:{item['label']}\n"
                if item.get("serviceType") == "SCA Service":
                    note += f"This might be an Integration connect:{item['label']}\n"
                if item.get("type") == "ECMConnector":
                    note += f"This might be an ECM connect:{item['label']}\n"
                if item.get("serviceType") == "Service Flow":
                    response_detail_2 = create_call_api(
                        f"visual/serviceModel/{item.get("poId")}", {"snapshotId": item.get("snapshotId")}
                    )
                    if response_detail_2["status"] == "200":
                        data_detail_2 = response_detail_2["data"]["items"]
                        for item in data_detail_2:
                            if item.get("serviceType") == "Integration Service":
                                note += f"This might be a Database call Store:{item['label']}\n"
                            if item.get("serviceType") == "SCA Service":
                                note += f"This might be an Integration connect:{item['label']}\n"



        # ghi_file_log(json.dumps(data), "a", "response Retrieve Model")
        # ghi_file_log(",\n", "a", "response Retrieve Model")

        return name_service, note
        # return {
        #     name_service,
        # }

    return "Không tìm thấy Service name", ""


def create_dataFrame(entries):
    timing_data = create_dataFrame_json(entries)

    return pd.DataFrame(timing_data)


def analyze_har(df_timings):

    # Calculate aggregate statistics
    aggregate_stats = df_timings.drop(columns=["status"]).describe()
    aggregate_stats.reset_index(inplace=True)

    # Identify slow requests (e.g., top 10% in terms of total time)
    slow_requests_threshold = df_timings["total_time"].quantile(0.9)
    slow_requests = df_timings[df_timings["total_time"] >= slow_requests_threshold]

    # Group by service/endpoint for breakdown
    # Here, we assume that the service/endpoint can be derived from the URL's path
    df_timings["service"] = df_timings["url"].apply(
        lambda x: x.split("/")[3] if len(x.split("/")) > 3 else "unknown"
    )
    service_breakdown = (
        df_timings.groupby("service")
        .agg({"total_time": ["count", "mean", "max"], "wait": ["mean", "max"]})
        .reset_index()
    )

    return aggregate_stats, slow_requests, service_breakdown



def calculate_total_duration(har_file):
    with open(har_file, "r", encoding="utf-8") as file:
        har_data = json.load(file)

    entries = har_data['log']['entries']

    if not entries:
        return 0, 0  # No entries found

    # Find the start time of the first request
    start_time = min(entry['startedDateTime'] for entry in entries)
    start_time = datetime.fromisoformat(start_time.replace('T', ' '))

    # Find the end time of the last request
    end_time = max(entry['startedDateTime'] for entry in entries)
    end_time = datetime.fromisoformat(end_time.replace('T', ' '))

    # Calculate the total duration
    total_duration = end_time - start_time
    total_seconds = total_duration.total_seconds()
    total_minutes = total_seconds // 60

    return int(total_seconds), int(total_minutes)


if __name__ == "__main__":
    """
    fol_cif_it_tk = []
    fol_cif_nhieu_tk = []
    list_har_file_it_tk = [
        "data_als_network/prod_do_time_tab/cif_ittk/1_kt_to_pre.har",
        "data_als_network/prod_do_time_tab/cif_ittk/2_pre_to_kt.har",
        "data_als_network/prod_do_time_tab/cif_ittk/3_kh_to_nn.har",
        "data_als_network/prod_do_time_tab/cif_ittk/4_nn_to_kv.har",
        "data_als_network/prod_do_time_tab/cif_ittk/5_kv_to_tc.har",
        "data_als_network/prod_do_time_tab/cif_ittk/6_tc_to_ts.har",
        "data_als_network/prod_do_time_tab/cif_ittk/7_ts_to_kqdg.har",
        "data_als_network/prod_do_time_tab/cif_ittk/8_kqdg_to_lich.har",
        "data_als_network/prod_do_time_tab/cif_ittk/9_lich_to_hs.har",
    ]

    list_har_file_nhieu_tk = [
        "data_als_network/prod_do_time_tab/cif_nhieutk/1_kt_to_pre.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/2_pre_to_kt.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/3_kh_to_nn.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/4_nn_to_kv.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/5_kv_to_tc.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/6_tc_to_ts.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/7_ts_to_kqdg.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/8_kqdg_to_lich.har",
        "data_als_network/prod_do_time_tab/cif_nhieutk/9_lich_to_hs.har",
    ]


    convert_file_name = [
        "Đồng ý khởi tạo đến màn hình Pre-screen",
        "Từ màn hình Pre-screen đến màn hình Khách hàng",
        "Từ màn hình khách hàng đến màn hình nghề nghiệp",
        "Từ màn hình Nghề nghiệp đến màn hình khoản vay",
        "Từ màn hình Khoản vay đến màn hình tài chính",
        "Từ màn hình Tài chính đến màn hình tài sản",
        "Từ màn hình Tài sản đến màn hình kết quả đánh giá",
        "Từ màn hình kết quả đánh giá đến màn hình lịch",
        "Từ màn hình lịch đến màn hình hồ sơ",
    ]


    for index, har_file in enumerate(list_har_file_it_tk):
        total_seconds, total_minutes = calculate_total_duration(har_file)
        fol_cif_it_tk.append((convert_file_name[index], total_minutes, total_seconds))

    df_fol_cif_it_tk = pd.DataFrame(fol_cif_it_tk, columns=["Screen transaction", "Total Minutes", "Total Seconds"])


    # I want to calculate the total duration of each list_har_file_it_tk and list_har_file_nhieu_tk
    # and save the results to an only 1 file Excel and rename the sheet to the name of the HAR file
    for index, har_file in enumerate(list_har_file_nhieu_tk):
        total_seconds, total_minutes = calculate_total_duration(har_file)
        fol_cif_nhieu_tk.append((convert_file_name[index], total_minutes, total_seconds))

    df_fol_cif_nhieu_tk = pd.DataFrame(fol_cif_nhieu_tk, columns=["Screen transaction", "Total Minutes", "Total Seconds"])
    
    # Define sheet names
    with pd.ExcelWriter(f"exports/Thống kê thời gian chuyển tab màn hình.xlsx") as writer:
        # Write each DataFrame to a different sheet
        df_fol_cif_it_tk.to_excel(writer, sheet_name="CIF ít tài khoản", index=False)
        df_fol_cif_nhieu_tk.to_excel(writer, sheet_name="CIF nhiều tài khoản", index=False)
    """

    list_action = [
        "data_als_network/prod/action/capnhatcore_ittk_kh.har",
        "data_als_network/prod/action/capnhatcore_ittk_taichinh.har",
        "data_als_network/prod/action/in_mau1_tudong.har",
        "data_als_network/prod/action/in_mau1.har",
        "data_als_network/prod/action/in_mau2_tudong.har",
        "data_als_network/prod/action/mau2.har",
        "data_als_network/prod/action/tudong_kqdg.har",
    ]
    fol_action = []
    for index, har_file in enumerate(list_action):
        total_seconds, total_minutes = calculate_total_duration(har_file)
        fol_action.append((har_file, total_minutes, total_seconds))

    df_fol_action = pd.DataFrame(fol_action, columns=["Screen transaction", "Total Minutes", "Total Seconds"])
    with pd.ExcelWriter(f"exports/Thống kê thời gian action.xlsx") as writer:
        # Write each DataFrame to a different sheet
        df_fol_action.to_excel(writer, sheet_name="Action", index=False)

    

    """
    folder_har_root = environ.get("FOLDER_HAR_ROOT")
    folder_har_partial = environ.get("FOLDER_HAR_PARTIAL")
    print('folder_har_partial:', folder_har_partial)

    FILE_NAME_EXCEL_ALL_REQUEST = f"tat_ca_cac_request_{folder_har_partial}_dongy_ra.xlsx"
    FILE_NAME_ANALYSIS = f"phan_tich_cac_thamso_{folder_har_partial}_dongy_ra.xlsx"

    HAR_FILE_PATH = f"{folder_har_root}/{folder_har_partial}/dongy_ra.har"

    entries = read_file(HAR_FILE_PATH)

    df_timings = create_dataFrame(entries)

    modify_column_df(df_timings, FILE_NAME_EXCEL_ALL_REQUEST)

    aggregate_stats, slow_requests, service_breakdown = analyze_har(df_timings)
    write_export_file(
        [aggregate_stats, slow_requests, service_breakdown], FILE_NAME_ANALYSIS
    )
    """



