//KH MOI
try {
    console.log('=============CIC LOS CUSTOMEER VK CK==========================');
    if (tw.local.lst_ER_Target != null && tw.local.lst_ER_Target.length > 0) {

        tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].PERIOD_REPORT = tw.local.lst_ER_Target[0].REPORT_TERM;

        tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].YEAR_ECONOMIC = tw.local.lst_ER_Target[0].REPORT_YEAR;

        tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].YEAR_REPORT = tw.local.lst_ER_Target[0].REPORT_YEAR;

        tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].QUARTERLY_REPORT = tw.local.lst_ER_Target[0].REPORT_QUARTER;
        tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].MONTH_REPORT = tw.local.lst_ER_Target[0].REPORT_MONTH;

        console.log('tw.local.data_process.LOS_LOAN.GROUP_SP:', tw.local.data_process.LOS_LOAN.GROUP_SP);
        for (var i = 0; i < tw.local.lst_ER_Target.length; i++) {
            //========================================================= BO THU NHAP

            if ((tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000001' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT == 'PR0000012')) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000019') {
                    tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].INFO_ECONOMIC_PERSONAL.TOTAL_MONTHLY_INCOME.push(tw.local.lst_ER_Target[i]);
                }
            } else if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000002' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000004' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000005' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000006' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000007' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000008' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000010' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000011' ||
                (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000003' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT == 'PR0000033') ||
                (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000003' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT == 'PR0000026') ||
                (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000009' && tw.local.data_process.LOS_LOAN.BIENPHAP_BAODAM == 'BPBDSEARCH002' &&
                    tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000083' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000084' &&
                    tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000089' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000103')
            ) {

                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000018') {

                    tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].INFO_ECONOMIC_PERSONAL.TOTAL_MONTHLY_INCOME.push(tw.local.lst_ER_Target[i]);
                }

            } else {

                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000002') {
                    tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].INFO_ECONOMIC_PERSONAL.TOTAL_MONTHLY_INCOME.push(tw.local.lst_ER_Target[i]);
                }
            }
            //========================================================= BO CHI PHI


            if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000003') {

                if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000009' && (tw.local.lst_ER_Target[i].CODE == 'CPCN010' ||
                    tw.local.lst_ER_Target[i].CODE == 'CPCN011')) {

                    tw.local.lst_ER_Target[i].VALUE_NUMBER = 0;
                }

                tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].INFO_ECONOMIC_PERSONAL.MONTHLY_COST_LIVING.push(tw.local.lst_ER_Target[i]);
            }


            //BO OT CHUNG
            if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000010') {
                tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].TBL_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                tw.local.out_ECONOMIC.INFO_ECONOMIC_ENTERPRISE[0].TBL_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);

            }

            //============================================= VOI SP TINCHAP =========================================================
            if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000009' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT == 'PR0000082') {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000011') {//TODO TG0000011
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            }
            else if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000001' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT == 'PR0000012') {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000013') {//TODO TG0000013
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            } else if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000001' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000012' ||
                tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000003' && tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000032'
            ) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000022') {//TODO TG0000022
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            } else if (tw.local.data_process.LOS_LOAN.GROUP_SP == 'GPR0000009' && tw.local.data_process.LOS_LOAN.BIENPHAP_BAODAM == 'BPBDSEARCH001' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000073' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000074' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000075' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000076' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000077' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT != 'PR0000078'
            ) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000024') {//TODO TG0000024
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            }
            else if (tw.local.data_process.LOS_LOAN.GROUP_SP === 'GPR0000009' && tw.local.data_process.LOS_LOAN.BIENPHAP_BAODAM === 'BPBDSEARCH001' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000073' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000074' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000075' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000076' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000077' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000078'
            ) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET === 'TG0000025') {//TODO TG0000025
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            }
            else if (tw.local.data_process.LOS_LOAN.GROUP_SP === 'GPR0000009' && tw.local.data_process.LOS_LOAN.BIENPHAP_BAODAM === 'BPBDSEARCH002' &&
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000083' ||
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000084' ||
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000089' ||
                tw.local.data_process.LOS_LOAN.LOAN_PRODUCT === 'PR0000103'
            ) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET === 'TG0000026') {//TODO TG0000026
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            } else if (tw.local.data_process.LOS_LOAN.GROUP_SP === 'GPR0000008' || tw.local.data_process.LOS_LOAN.GROUP_SP === 'GPR0000011' ||
                (tw.local.data_process.LOS_LOAN.GROUP_SP === 'GPR0000008' && tw.local.data_process.LOS_LOAN.GROUP_SP === 'PR0000060')
            ) {
                if (tw.local.lst_ER_Target[i].CODE_TARGET === 'TG0000030') {//TODO TG0000030
                    tw.local.data_process.ECONOMIC_RECORDS.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.data_process.ECONOMIC_RECORDS.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            }
            else {
                if (tw.local.lst_ER_Target[i].CODE_TARGET == 'TG0000020') {//TODO TG0000020
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.CODE_TARGET = tw.local.lst_ER_Target[i].CODE_TARGET;
                    tw.local.out_ECONOMIC.TBL_THE_SET_OF_TARGET.LIST_TARGET.push(tw.local.lst_ER_Target[i]);
                }
            }

        }

    }

    console.log('================Khoong taoj taif chinh o dday========');
} catch (err) {
    console.log('ERROR MAPPING TAI CHINH NGUOI DONG TRA NO : ', err);
}