var kq_1 = JSON.parse(tw.local.ket_qua_rule_ac)
var kq_2 = JSON.parse(tw.local.ket_qua_rule_ac_2)

var final_1 = kq_1.filter(function(el){
    return el.code == 'FINAL'
});
var final_2 = kq_2.filter(function(el){
    return el.code == 'FINAL'
});
var kq_chung = setKQ(final_1, final_2)   

[
	{
		"code": "FINAL",
		"ratio": 100.0,
		"numberValue": kq_chung.diem,
		"stringValue": kq_chung.str
	}
]


function setKQ(kq1, kq2){
    if(kq1 == "D" || kq2 == "D") return {str :"D", diem: 0};
    if(kq1 == "C" || kq2 == "C") return {str :"C", diem: 50};
    if(kq2 == "A" && kq2 == "A") return {str :"A", diem: 100};
}
