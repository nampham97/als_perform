try {
    var obj = {
        "GroupProduct": tw.local.data_process.LOS_LOAN.GROUP_SP,
        "Product": tw.local.Rule_ODM_DATA.LOAN.Product,
        "ColCurrency": getColUSD(tw.local.data_process.Collateral),
        // "ColValue": tw.local.Rule_ODM_DATA.LOAN.SumColValue,
        "CPCN022": tw.local.Rule_ODM_DATA.CUSTOMER.CPCN022,
        "DTCTD": tw.local.Rule_ODM_DATA.CUSTOMER.DTCTD,
        "ExpiredDate": tw.local.Rule_ODM_DATA.LOAN.ExpiredDate,
        "Income": tw.local.Rule_ODM_DATA.CUSTOMER.Income,
        "IncomeType": tw.local.Rule_ODM_DATA.CUSTOMER.IncomeType,
        "Nationality": tw.local.Rule_ODM_DATA.CUSTOMER.Nationality,
        "Position": tw.local.Rule_ODM_DATA.CUSTOMER.Position,
        "RL005": tw.local.Rule_ODM_DATA.CUSTOMER.RL005,
        "TNCN003": tw.local.Rule_ODM_DATA.CUSTOMER.TNCN003,
        "TNCN005": tw.local.Rule_ODM_DATA.CUSTOMER.TNCN005,
        "TNCN006": tw.local.Rule_ODM_DATA.CUSTOMER.TNCN006,
        "TNCN021": tw.local.Rule_ODM_DATA.CUSTOMER.TNCN021,
        "WorkTime": tw.local.Rule_ODM_DATA.CUSTOMER.WorkTime,
        "TotalIncome": tw.local.Rule_ODM_DATA.CUSTOMER.TotalIncome,
        "ACard": tw.local.data_process.RESULT_ODM.RESULT_ACARD_STR,
        "CardType": tw.local.data_process.LOS_LOAN.CARD_INFO.CARD_TYPE,
        "ConsumptionLimit": tw.local.Rule_ODM_DATA.LOAN.ConsumptionLimit,
        "CreateDate": tw.local.Rule_ODM_DATA.LOAN.CreateDate,
        "CreditLimit": tw.local.data_process.OPTION_DATA.DATAHUB.CreditLimit,
        "CreditLimitCC": tw.local.Rule_ODM_DATA.LOAN.CreditLimitCC,
        "WorkflowType": 'RLOS',
        "LoanPropose": tw.local.Rule_ODM_DATA.LOAN.LoanPropose,
        "LoanPropose_TKH": null,
        "CarPropose": getCardPropose(tw.local.data_process.LOS_LOAN.GROUP_SP, tw.local.data_process.LOS_LOAN.CARD_INFO.EXPECTED_CREDIT_LIMIT, tw.local.data_process.LOS_LOAN_BANKETHOP.LIST_THE_BANKETHOP[0]),
        "CardPropose": getCardPropose(tw.local.data_process.LOS_LOAN.GROUP_SP, tw.local.data_process.LOS_LOAN.CARD_INFO.EXPECTED_CREDIT_LIMIT, tw.local.data_process.LOS_LOAN_BANKETHOP.LIST_THE_BANKETHOP[0]),
        "LoanType": tw.local.Rule_ODM_DATA.LOAN.LoanType,
        "TermPropose": tw.local.Rule_ODM_DATA.LOAN.TermPropose,
        "UsedOverdraftLimitCC": tw.local.Rule_ODM_DATA.LOAN.UsedOverdraftLimitCC,
        "UsedOverdraftLimit": tw.local.Rule_ODM_DATA.LOAN.UsedOverdraftLimit,

        "CardLimitCC": tw.local.Rule_ODM_DATA.LOAN.CardLimitCC,
        "SumRealColValue": getSumRealColValue(tw.local.data_process.Collateral),
        "SumColValue": tw.local.Rule_ODM_DATA.LOAN.SumColValue,
        "ColUsedLimit": tw.local.Rule_ODM_DATA.LOAN.ColUsedLimit,
        "SumColUsedLimitHS": tw.local.Rule_ODM_DATA.LOAN.SumColUsedLimitHS,
        //   SumColValueHS_TS : tw.local.Rule_ODM_DATA.LOAN.SumColValue,
        //   SumColUsedLimitHS_TS : tw.local.Rule_ODM_DATA.LOAN.SumColUsedLimitHS,
        SumColValueHS_TS: getSumColValueHS_TS(tw.local.data_process.Collateral),
        SumColUsedLimitHS_TS: getSumColUsedHS_TS(tw.local.data_process.Collateral),
        MortgageLimit: tw.local.Rule_ODM_DATA.LOAN.MortgageLimit,
        "GroupColFinal": tw.local.data_process.RULE_OPTION.RCM,
        TotalCapitalNeeds: tw.local.data_process.LOS_LOAN.LOAN_TOTAL_DEMAND,
        "RelationshipOwner": tw.local.data_process.RULE_OPTION.RelationshipOwner,
        "CardLimit": tw.local.Rule_ODM_DATA.CUSTOMER.CardLimit,
        UsedLimitCard: tw.local.Rule_ODM_DATA.CUSTOMER.CardLimit,
        UsedLimitMortgage: tw.local.Rule_ODM_DATA.CUSTOMER.CardLimit,
        "TTD007": tw.local.Rule_ODM_DATA.CUSTOMER.TTD007,
        "TTD008": tw.local.Rule_ODM_DATA.CUSTOMER.TTD008,
        "TTD009": tw.local.Rule_ODM_DATA.CUSTOMER.TTD009,
        "SumColValueCard": 0,
        "ConsumptionLimitNew": tw.local.data_process.OPTION_DATA.DATAHUB.CreditLimitNew + tongTienCreditLimit(tw.local.data_process.LOS_LOAN.GROUP_SP, tw.local.Rule_ODM_DATA.LOAN.LoanPropose, getCardPropose(tw.local.data_process.LOS_LOAN.GROUP_SP, tw.local.data_process.LOS_LOAN.CARD_INFO.EXPECTED_CREDIT_LIMIT, tw.local.data_process.LOS_LOAN_BANKETHOP.LIST_THE_BANKETHOP[0])) + getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2, 'RL040', 'RL'),
        "MaxSumColValueNhaO": null,
        "ColSubTypeLevel1": null,
        "ColSubTypeLevel2": null,
        "LegalCol": null,
        "OutstandingBalanceUsed": tw.local.data_process.OPTION_DATA.outstandingBalance_TINCHAP,
        "UsedOverdraftLimitAll": null,
        "CurOutsBalMortgage": null,
        "CurOverdraftMortgage": null,
        "SpecificPosition": tw.local.data_process.LOS_LEGAL.CHUCVUCUTHE,
        "PolicyWorking": tw.local.data_process.LOS_LEGAL.DON_VI_CONG_TAC_AP_DUNG_CHINH_SACH,
        //  "TNCN024": tw.local.Rule_ODM_DATA.CUSTOMER.TN,
        "EmployeeBIDV": tw.local.data_process.LOS_CUSTOMER.NHAN_VIEN_THUOC_BIDV,
        "EmployeeIT": null,
        ActualUptime: getActualUptime(tw.local.data_process.LOS_LEGAL_V2.LOS_INFO_HOUSEHOLD_BUSINESS.TG_HOAT_DONG_THUC_TE_THANG, tw.local.data_process.LOS_LEGAL_V2.LOS_INFO_HOUSEHOLD_BUSINESS.TG_HOAT_DONG_THUC_TE_NAM),
        "OwnerCollateral": null,
        "RateCredit": null,
        "CusGroup": null,
        "AverageIncome": null,
        "CurCardLimit": null,
        "TargetCus": null,
        "CombineLoanType": null,
        "SumColValueHS": tw.local.Rule_ODM_DATA.LOAN.SumColValueHS,
        "LoanCountVIP1": null,
        "PolicyWoking": null,
        "DEP.GRP": null,
        SumColAllowcValueNhom04: getSumColAllowcValueNHOM(tw.local.data_process.Collateral, tw.local.data_process.RULE_OPTION.JP, 'NHOM04'),
        SumColAllowcValueNhom10: getSumColAllowcValueNHOM(tw.local.data_process.Collateral, tw.local.data_process.RULE_OPTION.JP, 'NHOM10'),
        SumColValueAllowc: getSumColValueAllowc(tw.local.data_process.Collateral),
        SumColUsedLimit: getSumColUsedLimit(tw.local.data_process.Collateral, tw.local.data_process.RULE_OPTION.ketquachung_rule_rocc, tw.local.data_process.RULE_OPTION.ketquachung_rule_blp),
        TotalCreditLimit: getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2.thongtin_sanxuatkinhdoanh, 'SXKD018', 'SXKD'),
        "SumLoanPropose": tw.local.data_process.LOS_LOAN.LOAN_AMOUNT_CONVERTED,
        LoanPurpose: tw.local.Rule_ODM_DATA.LOAN.LoanPurpose,
        CarStatus: tw.local.data_process.LOS_LOAN.LIST_TT_PA_VAYVON[0] ? tw.local.data_process.LOS_LOAN.LIST_TT_PA_VAYVON[0].MOTA_XE_OTO.tinhtrang_xe : "",
        CarOrigin: tw.local.data_process.LOS_LOAN.LIST_TT_PA_VAYVON[0] ? tw.local.data_process.LOS_LOAN.LIST_TT_PA_VAYVON[0].MOTA_XE_OTO.xuatxu : "",
        OutstandingBalanceUsed_TDBDS: tw.local.data_process.OPTION_DATA.DATAHUB.OutstandingBalanceUsed_TDBDS,
        UsedOverdraftLimit_TDBDS: tw.local.data_process.OPTION_DATA.DATAHUB.UsedOverdraftLimit_TDBDS,
        CreditLimit_TDBDS: tw.local.data_process.OPTION_DATA.DATAHUB.CreditLimit_TDBDS,
        CreditLimitNew: tw.local.data_process.OPTION_DATA.DATAHUB.CreditLimitNew,

        ACFinalResult: tw.local.Rule_ODM_DATA.PROCESS.ACFinalResult,
        SXKD014: getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2.thongtin_sanxuatkinhdoanh, 'SXKD014', 'SXKD'),
        SXKD015: getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2.thongtin_sanxuatkinhdoanh, 'SXKD015', 'SXKD'),
        SXKD016: getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2.thongtin_sanxuatkinhdoanh, 'SXKD016', 'SXKD'),
        SXKD017: getChitieu(tw.local.data_process.LOS_ECONOMIC_RECORDS_V2.thongtin_sanxuatkinhdoanh, 'SXKD017', 'SXKD'),
        ValuationOrganization: getValuationOrganization(tw.local.data_process.Collateral),
        LoanDemand: tw.local.data_process.LOS_LOAN.INFO_LOAN_TT_PA_VAYVON.nhucau_vayvon,
        SumColValueHS_NHOM04: tw.local.data_process.RULE_OPTION.Untitled,
        SumColUsedLimitHS_NHOM04: tw.local.data_process.RULE_OPTION.Untitled1,
        ColValue: Number(tw.local.data_process.RULE_OPTION.Untitled) || 0,
        SumColValueHS_NHOM034: tw.local.data_process.RULE_OPTION.Untitled2,
        SumColUsedLimitHS_NHOM034: tw.local.data_process.RULE_OPTION.Untitled3,
        GroupProperty : getGP(tw.local.data_process.RULE_OPTION.JP),
    };


    tw.local.Json_Input = JSON.stringify(obj);
} catch (err) {
    log.info('[ERROR]================== SP MAPPING =============');
    log.info(err);
    tw.local.Json_Input = JSON.stringify({
        errorMapping: err,
        obj: obj
    });
}

function getGP(gp){
	if(!gp || gp == "") return "";
	var arr_gp = JSON.parse(gp) || [];
	var kq = arr_gp.map(function(el){
		return el.stringValue;
	}).join(',');
	
	return kq;
}

function getTotalCapitalNeeds(lv, tongnhucauvon, list_hdmb) {
    if (lv === 'LV_10' || lv === 'LV_08') return tongnhucauvon;
    if (lv === 'LV_07') {
        if (!list_hdmb) return 0;
        var cur = 0;
        for (var i = 0; i < list_hdmb.length; i++) {
            if (list_hdmb[i].is_tinh_phaply) {
                cur += list_hdmb[i].giatri_hdmb;
            }
        }

        return cur;
    }
    return 0;
}

function getActualUptime(thang, nam) {
    if (!nam && !thang) return 0;
    if (!nam && thang) return 0 + thang;
    log.info('tinhan');
    if (!thang || thang == 0) return (nam * 12);
    log.info('tinhall')
    return thang + (nam * 12);
}

function sumLienket(list, Coeficient_Collateral) {
    var cur = 0;
    for (var i = 0; i < list.length; i++) {
        cur += list[i].Allotment_VND;
    }

    return cur * Coeficient_Collateral;
}

function getSumColUsedLimit(list, rocc, blp) {
    log.info("getSumColValueHS")
    if (list == undefined || list == null || list.length == 0) {
        return 0;
    }
    if (rocc == "") return 0;
    var kq_rocc = JSON.parse(rocc);
    kq_rocc = kq_rocc.filter(function (el) {
        return el.code != "FINAL";
    });
    if (blp != "") {
        var kq_blp = JSON.parse(blp);
        kq_blp = kq_blp.filter(function (el) {
            return el.code != "FINAL";
        });
    };

    var cur = 0;
    for (var i = 0; i < list.length; i++) {

        var num_rocc = kq_rocc[i] ? kq_rocc[i].numberValue : 100;
        var num_blp = kq_blp && kq_blp[i] ? kq_blp[i].numberValue : 100;
        if (num_rocc > 0 && num_blp > 0) {
            cur += sumLienket(list[i].Info_linked_Facility, list[i].Coeficient_Collateral);
        }


    }
    return cur;
}

function getSumColValueAllowc(list) {
    if (!list) return 0;
    var kq = 0;
    for (var i = 0; i < list.length; i++) {
        kq += list[i].Denomination_VND * list[i].Coeficient_Collateral;
    }
    return kq;
}

function getSumColAllowcValueNHOM(list, ruleGP, nhom) {
    //tw.local.data_process.Collateral[0].Coeficient_Collateral
    var kq = 0;
    if (ruleGP && ruleGP != "") {
        var list_nhom = JSON.parse(ruleGP);

        for (var i = 0; i < list_nhom.length; i++) {
            if (list_nhom[i].stringValue === nhom) {
                kq += list[i].Denomination_VND;
            }
        }
    }

    return kq;
}

function tongTienCreditLimit(gr, loanMoney, cardMoney) {
    if (!gr) return 0;
    if (gr === 'GPR0000009') return cardMoney

    return loanMoney;
}


function getValuationOrganization(list) {
    //	tw.local.data_process.Collateral[0].INFO_Collateral_TT_DINHGIA.donvi_dinhgia
    for (var i = 0; i < list.length; i++) {
        if (list[i].INFO_Collateral_TT_DINHGIA.donvi_dinhgia === 'TOCHUCDINHGIA001') {
            return 0;
        }
    }
    return 1;
}


function getChitieu(list, dieukien, group) {
    if (!list) return 0;
    if (list) {
        var list1 = [];
        if (group == 'TN') {
            list1 = list.INFO_ECONOMIC_PERSONAL.TOTAL_MONTHLY_INCOME || [];
        }
        if (group == 'CPCN') {
            list1 = list.INFO_ECONOMIC_PERSONAL.MONTHLY_COST_LIVING || [];
        }
        if (group == 'RL') {
            list1 = list.TBL_THE_SET_OF_TARGET.LIST_TARGET || [];
        }
        if (group == 'SXKD') {
            list1 = list.COCAUVON_PHUONGAN_KINHDOANH || [];
        }

        if (!list1) return -1;

        for (var i = 0; i < list1.length; i++) {
            if (list1[i].CODE == dieukien) {
                if (list1[i].CODE == dieukien) {
                    if (list1[i].TYPE_META_CODE == '4' || list1[i].TYPE_META_CODE == '3') {
                        return list1[i].VALUE;
                    }
                    if (list1[i].TYPE_META_CODE == '1') {
                        return list1[i].VALUE_NUMBER;
                    }

                    if (list1[i].TYPE_META_CODE == '6') {
                        return list1[i].VALUE_INTEGER;
                    }
                }
            }
        }
    }

    return -1;
}

function getCardPropose(gr, val, list) {
    //	tw.local.data_process.LOS_LOAN_BANKETHOP.LIST_THE_BANKETHOP[0].CARD_INFO.EXPECTED_CREDIT_LIMIT
    log.info('gr:' + gr);
    log.info('val:' + val);
    log.info(gr != 'GPR0000009' && (!val || val === 0));

    if (gr != 'GPR0000009' && (!val || val === 0)) {
        var kq = list ? list.CARD_INFO ? list.CARD_INFO.EXPECTED_CREDIT_LIMIT : 0 : 0;
        log.info('return cardpordporse kethop:' + kq);
        return kq;
    }

    return val;
}

function getSumColValueHS_TS(list) {
    if (!list) return 0;
    var cur = 0;
    for (var i = 0; i < list.length; i++) {
        log.info('thu : ' + i);
        log.info('list[i].Denomination_VND:' + list[i].Denomination_VND);
        log.info('list[i].Coeficient_Collateral: ' + list[i].Coeficient_Collateral);

        cur += list[i].Denomination_VND * list[i].Coeficient_Collateral * getDetermineCoefficient(list[i].Collateral_Type);
    }

    return cur;
}


function getSumColUsedHS_TS(list) {
    if (!list) return 0;
    var cur = 0;
    for (var i = 0; i < list.length; i++) {
        cur += sumColUsed(list[i].Info_linked_Facility) * list[i].Coeficient_Collateral * getDetermineCoefficient(list[i].Collateral_Type);
    }

    return cur;
}

function sumColUsed(list) {
    if (!list) return 0;
    var sumCol = 0;
    for (var i = 0; i < list.length; i++) {
        sumCol += list[i].Allotment_VND;
    }

    return sumCol;
}


function getDetermineCoefficient(type) {
    var determine_09 = '';
    determine_09 = tw.env.DetermineCoefficient_09;
    var arr09 = determine_09.split('-');

    if (arr09[1]) {
        var arr2 = arr09[1].split(',');
        for (var i = 0; i < arr2.length; i++) {
            if (type === arr2[i]) {
                log.info(arr09[0]);
                return Number(arr09[0]);
            }
        }
    }


    return Number(tw.env.DetermineCoefficient_08);

}


function getColUSD(list) {
    if (list == undefined || list == null || list.length == 0) {
        return null;
    }
    var cur = '';
    for (var i = 0; i < list.length; i++) {
        cur = list[i].Currency;
        if (list[i].Currency != 'VND') {
            break;
        }
    }

    return cur;
}

function getSumRealColValue(list) {
    if (list == undefined || list == null || list.length == 0) {
        return 0;
    }
    var cur = 0;
    for (var i = 0; i < list.length; i++) {
        cur += list[i].Denomination_VND || 0;
    }

    return cur;
}