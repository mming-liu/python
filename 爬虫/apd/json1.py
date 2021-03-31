import json
import jsonpath
import cx_Oracle
from jsonpath_ng import parse
# https://blog.csdn.net/nd211314555/article/details/88426529 jsonpath的基本操作

class get_message():
    def __init__(self,claim_no):
        self.claim_no = claim_no
    
    def get_message(self):
        conn = cx_Oracle.connect('apd_v50_test/apd_v50_test@192.168.200.25:1521/orcl')
        cursor = conn.cursor()
        result=cursor.execute(" select data from t_rule_audit_report_clm_model a where a.claim_id in (select b.claim_id from t_claim b where b.accident_no = '"+self.claim_no+"') order by a.modify_date desc" )
        data=cursor.fetchone()
        try:
            data = json.loads(str(data[0]))
            return data
        except :
            return None

class rule():
    def __init__(self,claim_no) -> None:
        self.claim_no = claim_no
        self.message = get_message(claim_no).get_message()
    
    # def get_data(self):
        self.coverageCode = jsonpath.jsonpath(self.message,expr='$.coverageCode')
        self.accidentType = jsonpath.jsonpath(self.message,expr='$.accLossInfo.accidentType')
        self.versionType = jsonpath.jsonpath(self.message,expr='$.claimWf.versionType')
        self.damageReason = jsonpath.jsonpath(self.message,expr='$.accLossInfo.damageReason')
        self.vehicleMakeCode = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.vehicleMakeCode')
        self.commercialCoverageList = jsonpath.jsonpath(self.message,expr='$.policyInfo.commercialCoverageList[*].coverageCode')
        self.compulsoryCoverageList = jsonpath.jsonpath(self.message,expr='$.policyInfo.compulsoryCoverageList[*].coverageCode')    
        self.totalEstimateAmount = jsonpath.jsonpath(self.message,expr='$.feeInfo.totalEstimateAmount.currentSubmitValue')
        self.damageDate = jsonpath.jsonpath(self.message,expr='$.claimWf.damageDate')
        self.lossVehicleType = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.lossVehicleType')
        self.compulsoryPolicyEndDate = jsonpath.jsonpath(self.message,expr='$.policyInfo.compulsoryPolicyEndDate')
        self.commercialPolicyEndDate = jsonpath.jsonpath(self.message,expr= '$.policyInfo.commercialPolicyEndDate')
        self.standardPartId = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].standardPartId')
        self.partName = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partName')
        self.manualFlag = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].manualFlag')
        self.manualMatchedUniquePart_standardid = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].manualMatchedUniquePart.standardPartId')
        self.manualMatchedUniquePart_partName = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].manualMatchedUniquePart.partName')
        self.operationType = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].operationType.currentSubmitValue')
        self.claimEstimateItemId = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].claimEstimateItemId')
        self.partFeeDiscount = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partFeeDiscount.currentSubmitValue')
        self.repairFeeDiscount = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].repairFeeDiscount.currentSubmitValue')
        self.paintFeeDiscount = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].paintFeeDiscount.currentSubmitValue')
        self.allPaintFeeSum = jsonpath.jsonpath(self.message,expr='$.feeInfo.allPaintFeeSum.currentSubmitValue')
        self.removeFeeDiscount = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].removeFeeDiscount.currentSubmitValue')
        self.allRemoveFeeSum = jsonpath.jsonpath(self.message,expr='$.feeInfo.allRemoveFeeSum.currentSubmitValue')
        self.wholePaintFLag = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].wholePaintFLag')
        self.outerFlag_source = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.outerFlag.valueSource')
        self.outerFlag_instantValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.outerFlag.instantValue')
        self.outerFlag_standardValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.outerFlag.standardValue')
        self.outerFlag_seriesValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.outerFlag.seriesValue')
        self.materialCode = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimMaterialList[*].materialCode')
        self.materialName = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimMaterialList[*].materialName')
        self.materialTotalAmount = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimMaterialList[*].materialTotalAmount.currentSubmitValue')

    def rule_0101010005(self):
        print(self.coverageCode)
        print(self.commercialCoverageList,self.compulsoryCoverageList)
        print(self.damageReason)
        print(self.vehicleMakeCode)
        print(self.partName)
        print(self.standardPartId)
        print(self.manualFlag)
        print(self.manualMatchedUniquePart_standardid)
        print(self.manualMatchedUniquePart_partName)
        print(self.operationType)
        print(self.partFeeDiscount)
        print(self.repairFeeDiscount)
        print(self.removeFeeDiscount)
        print(self.paintFeeDiscount)

    def rule_0101010006(self):
        print(self.versionType)
        print(self.commercialCoverageList,self.compulsoryCoverageList)
        print(self.lossVehicleType)
        print(self.accidentType)
        print(self.allPaintFeeSum)
        print(self.allRemoveFeeSum)
        print(self.claimEstimateItemId)
        print(self.operationType)
        print(self.paintFeeDiscount)
        print(self.wholePaintFLag)
        print(self.outerFlag_source)
        print(self.outerFlag_instantValue)
        print(self.outerFlag_standardValue)
        print(self.outerFlag_seriesValue)

    def rule_0101010007(self):
        print(self.commercialCoverageList,self.compulsoryCoverageList)
        print(self.lossVehicleType)
        print(self.damageReason)

    def rule_0101010008(self):
        print(self.lossVehicleType)
        print(self.commercialCoverageList,self.compulsoryCoverageList)
        print(self.damageReason)
        print(self.partName)
        print(self.standardPartId)
        print(self.manualFlag)
        print(self.manualMatchedUniquePart_standardid)
        print(self.manualMatchedUniquePart_partName)
        print(self.operationType)
        print(self.partFeeDiscount)
        print(self.repairFeeDiscount)
        print(self.removeFeeDiscount)
        print(self.paintFeeDiscount) 

    def rule_0101010010(self):
        print(self.versionType)
        print(self.commercialCoverageList,self.compulsoryCoverageList)
        print(self.lossVehicleType)
        print(self.claimEstimateItemId)
        print(self.partName)
        print(self.standardPartId)
        print(self.manualFlag)
        print(self.manualMatchedUniquePart_standardid)
        print(self.manualMatchedUniquePart_partName)
        print(self.operationType)
        print(self.partFeeDiscount)
        print(self.repairFeeDiscount)
        print(self.removeFeeDiscount)
        print(self.paintFeeDiscount)     
        print(self.materialCode)
        print(self.materialName)
        print(self.materialTotalAmount)    

if __name__ == '__main__':
    claim_no = 'acc_20210326_001'
    rule_0101010005 = rule(claim_no).rule_0101010010()



# path = 'C:/Users/ccc/Desktop/APD/5.0报文/处理损失项目.txt'
# with open(path,'r',encoding='utf-8') as f:
#     data = f.read()
#     data = eval(data)
#     # print(data)

# laborValue1 = jsonpath.jsonpath(data,expr='$.claimLabors[*].laborFeeAfterDiscount')
# laborValue2 = jsonpath.jsonpath(data,expr='$.claimLabors[*].operationType')

# partQuantity = jsonpath.jsonpath(data,expr='$.claimParts[*].partQuantity')
# unitPrice = jsonpath.jsonpath(data,expr='$.claimParts[*].unitPrice')

# print(partQuantity,unitPrice)
# lenth = len(partQuantity)
# print(lenth)
# if lenth >= 1 :
#     for i in range(1,lenth+1):
#         print(i, i % 2)
#         if i % 2== 1:
#             path = '$.claimParts['+str(i-1)+'].partQuantity'
#             part_quantity = partQuantity[i-1]+2
#             jsonpath_expr  = parse(path)
#             jsonpath_expr.find(data)
#             updated_json = jsonpath_expr.update(data, part_quantity)
#         else :
#             path = '$.claimParts['+str(i-1)+'].unitPrice'
#             unit_Price = unitPrice[i-1]+1000
#             jsonpath_expr  = parse(path)
#             jsonpath_expr.find(data)
#             updated_json = jsonpath_expr.update(data, unit_Price)

# for m in laborValue2:
#     if m == '03':
#         # print(laborValue2.index(m))
#         path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFee'
#         # print(path)
#         paint_fee = laborValue1[laborValue2.index(m)]+1000
#         jsonpath_expr  = parse(path)
#         jsonpath_expr.find(data)
#         updated_json = jsonpath_expr.update(data, paint_fee)
#         # list的值重复时，只能去到第一个index，所以该list中的值，才能取到符合条件的下一个值
#         laborValue2[laborValue2.index(m)] = '05'
#     elif m == '02' or m == '04':
#         path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFeeAfterDiscount'
#         # print(path)
#         labor_fee = laborValue1[laborValue2.index(m)]+1000
#         jsonpath_expr  = parse(path)
#         jsonpath_expr.find(data)
#         updated_json = jsonpath_expr.update(data, labor_fee)
#         # list的值重复时，只能去到第一个index，所以该list中的值，才能取到符合条件的下一个值
#         laborValue2[laborValue2.index(m)] = '05'

# print(data)