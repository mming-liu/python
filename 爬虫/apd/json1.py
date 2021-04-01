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
        self.vehicleSeriesCode = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.vehicleSeriesCode')
        self.vehicleHash_current = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.vehicleHash.currentSubmitValue')
        self.vehicleHash_lastSubmitValue = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.vehicleHash.lastSubmitValue')
        self.commercialCoverageList = jsonpath.jsonpath(self.message,expr='$.policyInfo.commercialCoverageList[*].coverageCode')
        self.compulsoryCoverageList = jsonpath.jsonpath(self.message,expr='$.policyInfo.compulsoryCoverageList[*].coverageCode')    
        self.totalEstimateAmount = jsonpath.jsonpath(self.message,expr='$.feeInfo.totalEstimateAmount.currentSubmitValue')
        self.damageDate = jsonpath.jsonpath(self.message,expr='$.claimWf.damageDate')
        self.lossVehicleType = jsonpath.jsonpath(self.message,expr='$.vehicleInfo.lossVehicleType')
        self.compulsoryPolicyEndDate = jsonpath.jsonpath(self.message,expr='$.policyInfo.compulsoryPolicyEndDate')
        self.commercialPolicyEndDate = jsonpath.jsonpath(self.message,expr= '$.policyInfo.commercialPolicyEndDate')
        self.standardPartId = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].standardPartId')
        self.partName = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partName')
        self.partId = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partId')
        self.quantity_current = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].quantity.currentSubmitValue')
        self.quantity_lastSubmitValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].quantity.lastSubmitValue')
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
        self.assemblyPartRelFlag = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartRelFlag.valueSource')
        self.assemblyPartIds_valueSource = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartIds.valueSource')
        self.assemblyPartIds_instantValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartIds.instantValue')
        self.assemblyPartIds_standardValue = jsonpath.jsonpath(self.message,expr='$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartIds.standardValue')

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
   
    def rule_0104010003(self):
        print(1,self.versionType)
        print(2,self.vehicleMakeCode)
        print(3,self.vehicleSeriesCode)    
        print(4,self.partFeeDiscount)
        print(5,self.repairFeeDiscount)
        print(6,self.removeFeeDiscount)
        print(7,self.paintFeeDiscount)   
        print(8,self.claimEstimateItemId)
        print(9,self.partName)
        print(10,self.partId)
        print(11,self.standardPartId)
        print(12,self.assemblyPartRelFlag)
        print(13,self.assemblyPartIds_valueSource)
        print(14,self.assemblyPartIds_instantValue)
        print(15,self.assemblyPartIds_standardValue)

    def rule_0107010040(self):
        print(1,self.vehicleHash_current)
        print(2,self.vehicleHash_lastSubmitValue)
        print(3,self.partName)
        print(4,self.quantity_current)
        print(5,self.quantity_lastSubmitValue)

if __name__ == '__main__':
    claim_no = 'acc_20210401_003'
    rule_0101010005 = rule(claim_no).rule_0107010040()