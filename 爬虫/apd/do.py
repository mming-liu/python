import json
import re
import jsonpath
import cx_Oracle
from jsonpath_ng import parse

class get_message():
    def __init__(self,claim_no):
        self.claim_no = claim_no
    
    def get_message(self):
        conn = cx_Oracle.connect('apd_v50_test/apd_v50_test@192.168.200.25:1521/orcl')
        cursor = conn.cursor()
        result=cursor.execute(" select data from t_rule_audit_report_clm_model a where a.claim_id in (select b.claim_id from t_claim b where b.claim_no = '"+self.claim_no+"') order by a.modify_date desc" )
        data=cursor.fetchone()
        try:
            data = json.loads(str(data[0]))
            return data
        except :
            return None
    
    def get_data(self,path):
        data = jsonpath.jsonpath(self.get_message(),expr=path)
        return data

class get_data(get_message):   
    def __init__(self, claim_no):
        super().__init__(claim_no)

    def accident_no (self):
        accident_no = super().get_data('$.accLossInfo.accidentNo')
        # str() 将list类型转成字符串；或者使用str()
        return 'accident = '+str(accident_no)   
    
    def claim_version(self):
        claim_version = super().get_data('$.claimWf.claimVersion')
        return 'claim_version = '+str(claim_version)
    
    def report_date(self):
        report_date = super().get_data('$.claimWf.reportDate')
        return 'report_date = '+str(report_date)
    
    def reportFirstSiteFlag(self):
        reportFirstSiteFlag = super().get_data('$.accLossInfo.reportFirstSiteFlag')
        return 'reportFirstSiteFlag = '+str(reportFirstSiteFlag)
    
    def repairFactoryType_current(self):
        repairFactoryType_current = super().get_data('$.repairFactoryInfo.repairFactoryType.currentSubmitValue')
        return 'repairFactoryType_current = '+str(repairFactoryType_current)
    
    def repairFactoryType_firstComplete(self):
        repairFactoryType_firstComplete = super().get_data('$.repairFactoryInfo.repairFactoryType.firstVersionEstReiCompleteValue')
        return 'repairFactoryType_firstComplete = '+str(repairFactoryType_firstComplete)

    def vin(self):
        vin = super().get_data('$.vehicleInfo.vin')
        return 'vin = '+str(vin)
    
    def collisionPoints(self):
        collisionPoints = super().get_data('$.vehicleInfo.collisionPoints')
        return 'collisionPoints = '+str(collisionPoints)

    def lossDegree_current(self):
        lossDegree = super().get_data('$.vehicleInfo.lossDegree.currentSubmitValue')
        return 'lossDegree_current = '+str(lossDegree)
    
    def plateNo(self):
        plateNo = super().get_data('$.vehicleInfo.plateNo')
        return 'plateNo = '+str(plateNo)
    
    def bodyInjuryFlag(self):
        bodyInjuryFlag = super().get_data('$.accLossInfo.bodyInjuryFlag')
        return 'bodyInjuryFlag = '+str(bodyInjuryFlag)
    
    def brandModel(self):
        brandModel = super().get_data('$.vehicleInfo.brandModel')
        return 'brandModel = '+str(brandModel)
    
    def engineNo(self):
        engineNo = super().get_data('$.vehicleInfo.engineNo')
        return 'engineNo = '+str(engineNo)
    
    def purchasePrice(self):
        purchasePrice = super().get_data('$.vehicleInfo.purchasePrice')
        return 'purchasePrice = '+str(purchasePrice)
    
    def vehicleSubModelName_current(self):
        vehicleSubModelName_current = super().get_data('$.vehicleInfo.vehicleSubModelName.currentSubmitValue')
        return 'vehicleSubModelName_current = '+str(vehicleSubModelName_current)
    
    def commercialCoverageList(self):
        commercialCoverageList = super().get_data('$.policyInfo.commercialCoverageList[*]')
        return 'commercialCoverageList = '+str(commercialCoverageList)
    
    def compulsoryCoverageList (self):
        compulsoryCoverageList = super().get_data('$.policyInfo.compulsoryCoverageList[*]')  
        return 'compulsoryCoverageList = '+str(compulsoryCoverageList)
    
    def compulsoryPolicyNo (self):
        compulsoryPolicyNo = super().get_data('$.policyInfo.compulsoryPolicyNo')
        return 'compulsoryPolicyNo = '+str(compulsoryPolicyNo)
   
    def compulsoryVehicleVin(self):
        compulsoryVehicleVin = super().get_data('$.policyInfo.compulsoryVehicleVin')
        return 'compulsoryVehicleVin = '+str(compulsoryVehicleVin)
    
    def commercialVehicleVin(self):
        commercialVehicleVin = super().get_data('$.policyInfo.commercialVehicleVin')
        return 'commercialVehicleVin = '+str(commercialVehicleVin)
    
    def compulsoryVehiclePlateNo(self):
        compulsoryVehiclePlateNo = super().get_data('$.policyInfo.compulsoryVehiclePlateNo')
        return 'compulsoryVehiclePlateNo = '+str(compulsoryVehiclePlateNo)
    
    def compulsoryVehicleSubModel(self):
        compulsoryVehicleSubModel = super().get_data('$.policyInfo.compulsoryVehicleSubModel')
        return 'compulsoryVehicleSubModel = '+str(compulsoryVehicleSubModel)
    
    def compulsoryVehicleBrandModel(self):
        compulsoryVehicleBrandModel = super().get_data('$.policyInfo.compulsoryVehicleBrandModel')
        return 'compulsoryVehicleBrandModel = '+str(compulsoryVehicleBrandModel)

    def compulsoryVehicleEngineNo(self):
        compulsoryVehicleEngineNo = super().get_data('$.policyInfo.compulsoryVehicleEngineNo')
        return 'compulsoryVehicleEngineNo = '+str(compulsoryVehicleEngineNo)
    
    def compulsoryPolicyStartDate(self): 
        compulsoryPolicyStartDate= super().get_data('$.policyInfo.compulsoryPolicyStartDate')  
        return 'compulsoryPolicyStartDate = '+str(compulsoryPolicyStartDate)
    
    def compulsoryRenewPolicyFlag(self):
        compulsoryRenewPolicyFlag = super().get_data('$.policyInfo.compulsoryRenewPolicyFlag') 
        return 'compulsoryRenewPolicyFlag = '+str(compulsoryRenewPolicyFlag)

    def compulsoryPolicyEndDate(self):
        compulsoryPolicyEndDate = super().get_data('$.policyInfo.compulsoryPolicyEndDate')
        return 'compulsoryPolicyEndDate = '+str(compulsoryPolicyEndDate)
    
    def commercialRenewPolicyFlag(self):
        commercialRenewPolicyFlag = super().get_data('$.policyInfo.commercialRenewPolicyFlag')
        return 'commercialRenewPolicyFlag = '+str(commercialRenewPolicyFlag)

    def commercialPolicyEndDate(self):
        commercialPolicyEndDate = super().get_data( '$.policyInfo.commercialPolicyEndDate')
        return 'commercialPolicyEndDate = '+str(commercialPolicyEndDate)

    def commercialPolicyStartDate(self):
        commercialPolicyStartDate = super().get_data('$.policyInfo.commercialPolicyStartDate')
        return 'commercialPolicyStartDate = '+str(commercialPolicyStartDate) 
    
    def commercialVehiclePlateNo(self):
        commercialVehiclePlateNo = super().get_data('$.policyInfo.commercialVehiclePlateNo')
        return 'commercialVehiclePlateNo = '+str(commercialVehiclePlateNo)
    
    def commercialVehicleSubModel(self):
        commercialVehicleSubModel = super().get_data('$.policyInfo.commercialVehicleSubModel')
        return 'commercialVehicleSubModel = '+str(commercialVehicleSubModel)
    
    def commercialVehicleBrandModel(self):
        commercialVehicleBrandModel = super().get_data('$.policyInfo.commercialVehicleBrandModel')
        return 'commercialVehicleBrandModel = '+str(commercialVehicleBrandModel)
    
    def commercialVehicleEngineNo(self):
        commercialVehicleEngineNo = super().get_data('$.policyInfo.commercialVehicleEngineNo')
        return 'commercialVehicleEngineNo = '+str(commercialVehicleEngineNo)
    
    def commercialPolicyNo (self):
        commercialPolicyNo = super().get_data('$.policyInfo.commercialPolicyNo')
        return 'commercialPolicyNo = '+str(commercialPolicyNo)
    
    def contactInfoList(self):
        contactInfoList = super().get_data('$.contactInfoList[*]')
        return 'contactInfoList = '+str(contactInfoList)

    def includeTypeList(self):    
        includeTypeList = super().get_data('$.vehicleInfo.includeTypeList')
        return 'includeTypeList = '+str(includeTypeList)
    
    def surveyFirstSiteFlag(self):
        surveyFirstSiteFlag = super().get_data('$.accLossInfo.surveyFirstSiteFlag')
        return 'surveyFirstSiteFlag = '+str(surveyFirstSiteFlag)
    
    def coverageCode(self):
        coverageCode = super().get_data('$.coverageCode')
        return 'coverageCode = '+str(coverageCode)
    
    def accidentType(self):
        accidentType = super().get_data('$.accLossInfo.accidentType')
        return 'accidentType = '+str(accidentType)
    
    def versionType(self):
        versionType = super().get_data('$.claimWf.versionType')
        return 'versionType = '+str(versionType)
    
    def damageReason(self):
        damageReason = super().get_data('$.accLossInfo.damageReason')
        return 'damageReason = '+str(damageReason)
    
    def vehicleMakeCode(self):
        vehicleMakeCode = super().get_data('$.vehicleInfo.vehicleMakeCode')
        return 'vehicleMakeCode = '+str(vehicleMakeCode)
    
    def vehicleSeriesCode(self):
        vehicleSeriesCode = super().get_data('$.vehicleInfo.vehicleSeriesCode')
        return 'vehicleSeriesCode = '+str(vehicleSeriesCode)
    
    def vehicleHash_current(self):
        vehicleHash_current = super().get_data('$.vehicleInfo.vehicleHash.currentSubmitValue')
        return 'vehicleHash_current = '+str(vehicleHash_current)
    
    def vehicleHash_last(self):
        vehicleHash_last = super().get_data('$.vehicleInfo.vehicleHash.lastSubmitValue')
        return 'vehicleHash_last = '+str(vehicleHash_last)

    def vehicleHash_firstComplete(self):
        '''
        首次定核损结束的定型信息
        '''
        vehicleHash_first = super().get_data('$.vehicleInfo.vehicleHash.firstVersionEstReiCompleteValue')
        return 'vehicleHash_firstComplete = '+str(vehicleHash_first)
    
    def totalEstimateAmount(self):
        totalEstimateAmount = super().get_data('$.feeInfo.totalEstimateAmount.currentSubmitValue')
        return 'totalEstimateAmount = '+str(totalEstimateAmount)
    
    def damageDate(self):
        damageDate = super().get_data('$.claimWf.damageDate')
        return 'damageDate = '+str(damageDate)
    
    def lossVehicleType(self):
        lossVehicleType = super().get_data('$.vehicleInfo.lossVehicleType')
        return 'lossVehicleType = '+str(lossVehicleType)
    
    def partAmt_current(self):
        partAmt_current = super().get_data('$.feeInfo.partAmt.currentSubmitValue')
        return 'partAmt_current = '+str(partAmt_current)
    
    def partAmt_firstComplete(self):
        '''
        首次定核损结束时的总配件费
        '''
        partAmt_first = super().get_data('$.feeInfo.partAmt.firstVersionEstReiCompleteValue')
        return 'partAmt_firstComplete = '+str(partAmt_first)
    
    def laborAmt_current(self):
        laborAmt_current =super().get_data('$.feeInfo.laborAmt.currentSubmitValue')
        return 'laborAmt_current = '+str(laborAmt_current)
    
    def laborAmt_firstComplete(self):
        '''
        首次定核损结束时总的工时费
        '''
        laborAmt_firstComplete = super().get_data('$.feeInfo.laborAmt.firstVersionEstReiCompleteValue')
        return 'laborAmt_firstComplete = '+str(laborAmt_firstComplete)

    def claimPartList_standardPartId(self):
        standardPartId = super().get_data('$.lossInfo.claimPartList[*].standardPartId')
        return 'claimPartList_standardPartId = '+str(standardPartId)
    
    def claimPartList_partName(self):
        partName = super().get_data('$.lossInfo.claimPartList[*].partName')
        return 'claimPartList_partName = '+str(partName)
    
    def claimPartList_partId(self):
        partId = super().get_data('$.lossInfo.claimPartList[*].partId')
        return 'claimPartList_partId = '+str(partId)
    
    def claimPartList_quantity_current(self):
        quantity_current = super().get_data('$.lossInfo.claimPartList[*].quantity.currentSubmitValue')
        return 'claimPartList_quantity_current = '+str(quantity_current)
    
    def claimPartList_quantity_last(self):
        quantity_lastSubmitValue = super().get_data('$.lossInfo.claimPartList[*].quantity.lastSubmitValue')
        return 'claimPartList_quantity_last = '+str(quantity_lastSubmitValue)
    
    def claimPartList_manualFlag(self):
        manualFlag = super().get_data('$.lossInfo.claimPartList[*].manualFlag')
        return 'claimPartList_manualFlag = '+str(manualFlag)
    
    def claimPartList_itemTotalFeeDiscount_current(self):
        itemTotalFeeDiscount_current = super().get_data('$.lossInfo.claimPartList[*].itemTotalFeeDiscount.currentSubmitValue')
        return 'claimPartList_itemTotalFeeDiscount_current = '+str(itemTotalFeeDiscount_current)

    def claimPartList_unitPriceDiscount_current(self):
        unitPriceDiscount_current = super().get_data('$.lossInfo.claimPartList[*].unitPriceDiscount.currentSubmitValue')
        return 'claimPartList_unitPriceDiscount_current = '+str(unitPriceDiscount_current)
    
    def claimPartList_unitPriceDiscount_last(self):
        unitPriceDiscount_last = super().get_data('$.lossInfo.claimPartList[*].unitPriceDiscount.lastSubmitValue')
        return 'claimPartList_unitPriceDiscount_last = '+str(unitPriceDiscount_last)
    
    def claimPartList_part_current(self):
        claimPartList_part = super().get_data('$.lossInfo.claimPartList[*].partType.currentSubmitValue')
        return 'claimPartList_part_current = '+str(claimPartList_part)

    def claimPartList_part_last(self):
        claimPartList_part = super().get_data('$.lossInfo.claimPartList[*].partType.lastSubmitValue')
        return 'claimPartList_part_last = '+str(claimPartList_part)
    
    def manualMatchedUniquePart_standardId(self):
        manualMatchedUniquePart_standardid = super().get_data('$.lossInfo.claimPartList[*].manualMatchedUniquePart.standardPartId')
        return 'manualMatchedUniquePart_standardId = '+str(manualMatchedUniquePart_standardid)
    
    def manualMatchedUniqueStandardPartList_partName(self):
        manualMatchedUniqueStandardPartList_partName = super().get_data('$.lossInfo.claimPartList[*].manualMatchedStandardPartList.partName')
        return 'manualMatchedUniqueStandardPartList_partName = '+str(manualMatchedUniqueStandardPartList_partName)
    
    def manualMatchedUniquePart_partName(self):
        manualMatchedUniquePart_partName = super().get_data('$.lossInfo.claimPartList[*].manualMatchedUniquePart.partName')
        return 'manualMatchedUniquePart_partName = '+str(manualMatchedUniquePart_partName)
    
    def manualMatchedUniquePart_partNo(self):
        manualMatchedUniquePart_partNo = super().get_data('$.lossInfo.claimPartList[*].manualMatchedUniquePart.partNo')
        return 'manualMatchedUniquePart_partNo = '+str(manualMatchedUniquePart_partNo)
    
    def manualMatchedUniquePart_partId(self):
        manualMatchedUniquePart_partId = super().get_data('$.lossInfo.claimPartList[*].manualMatchedUniquePart.partId')
        return 'manualMatchedUniquePart_partId = '+str(manualMatchedUniquePart_partId)
    
    def claimPartList_operationType(self):
        operationType = super().get_data('$.lossInfo.claimPartList[*].operationType.currentSubmitValue')
        return 'claimPartList_operationType = '+str(operationType)
    
    def claimPartList_claimEstimateItemId(self):
        claimEstimateItemId = super().get_data('$.lossInfo.claimPartList[*].claimEstimateItemId')
        return 'claimPartList_claimEstimateItemId = '+str(claimEstimateItemId)
    
    def claimPartList_partNo(self):
        partNo = super().get_data('$.lossInfo.claimPartList[*].partNo')
        return 'claimPartList_partNo = '+str(partNo)
    
    def claimPartList_partFeeDiscount_current(self):
        partFeeDiscount_current = super().get_data('$.lossInfo.claimPartList[*].partFeeDiscount.currentSubmitValue')
        return 'claimPartList_partFeeDiscount_current = '+str(partFeeDiscount_current)
    
    def claimPartList_partFeeDiscount_firstComplete(self):
        '''
        首次定核损结束的单个配件费
        '''
        partFeeDiscount_first = super().get_data('$.lossInfo.claimPartList[*].partFeeDiscount.firstVersionEstReiCompleteValue')
        return 'claimPartList_partFeeDiscount_firstComplete = '+str(partFeeDiscount_first)
    
    def claimPartList_repairFeeDiscount_current(self):
        repairFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].repairFeeDiscount.currentSubmitValue')
        return 'claimPartList_repairFeeDiscount_current = '+str(repairFeeDiscount)
    
    def claimPartList_repairFeeDiscount_firstComplete(self):
        repairFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].repairFeeDiscount.firstVersionEstReiCompleteValue')
        return 'claimPartList_repairFeeDiscount_firstComplete = '+str(repairFeeDiscount)
    
    def claimPartList_paintFeeDiscount_current(self):
        paintFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].paintFeeDiscount.currentSubmitValue')
        return 'claimPartList_paintFeeDiscount_current = '+str(paintFeeDiscount)
    
    def claimPartList_paintFeeDiscount_firstComplete(self):
        paintFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].paintFeeDiscount.firstVersionEstReiCompleteValue')
        return 'claimPartList_paintFeeDiscount_firstComplete = '+str(paintFeeDiscount)
    
    def allPaintFeeSum(self):
        allPaintFeeSum = super().get_data('$.feeInfo.allPaintFeeSum.currentSubmitValue')
        return 'allPaintFeeSum = '+str(allPaintFeeSum)
    
    def claimPartList_removeFeeDiscount_current(self):
        removeFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].removeFeeDiscount.currentSubmitValue')
        return 'claimPartList_removeFeeDiscount_current = '+str(removeFeeDiscount)

    def claimPartList_removeFeeDiscount_firstComplete(self):
        removeFeeDiscount = super().get_data('$.lossInfo.claimPartList[*].removeFeeDiscount.firstVersionEstReiCompleteValue')
        return 'claimPartList_removeFeeDiscount_current = '+str(removeFeeDiscount)
    
    def claimPartList_allRemoveFeeSum_current(self):
        allRemoveFeeSum = super().get_data('$.feeInfo.allRemoveFeeSum.currentSubmitValue')
        return 'claimPartList_allRemoveFeeSum_current = '+str(allRemoveFeeSum)
    
    def wholePaintFLag(self):
        wholePaintFLag = super().get_data('$.lossInfo.claimPartList[*].wholePaintFLag')
        return 'wholePaintFLag = '+str(wholePaintFLag)
    
    def outerFlag(self):
        outerFlag = super().get_data('$.lossInfo.claimPartList[*].partAttribInfo.outerFlag')
        return 'outerFlag = '+str(outerFlag)
    
    def assemblyPartRelFlag(self):
        assemblyPartRelFlag = super().get_data('$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartRelFlag.valueSource')
        return 'assemblyPartRelFlag = '+str(assemblyPartRelFlag)
    
    def assemblyPartIds(self):
        assemblyPartIds = super().get_data('$.lossInfo.claimPartList[*].partAttribInfo.assemblyPartIds')
        return 'assemblyPartIds = '+str(assemblyPartIds)
    
    def glassFlag(self):
        glassFlag = super().get_data('$.lossInfo.claimPartList[*].partAttribInfo.glassFlag')
        return 'glassFlag = '+str(glassFlag)
    
    def claimMaterialList_claimEstimateItemId(self):
        claimMaterialList_claimEstimateItemId = super().get_data('$.lossInfo.claimMaterialList[*].claimEstimateItemId')
        return 'claimMaterialList_claimEstimateItemId = '+str(claimMaterialList_claimEstimateItemId)

    def claimMaterialList_materialCode(self):    
        claimMaterialList_materialCode = super().get_data('$.lossInfo.claimMaterialList[*].materialCode')
        return 'claimMaterialList_materialCode = '+str(claimMaterialList_materialCode)
    
    def claimMaterialList_materialName(self):
        claimMaterialList_materialName = super().get_data('$.lossInfo.claimMaterialList[*].materialName')
        return 'claimMaterialList_materialName = '+str(claimMaterialList_materialName)

    def claimMaterialList_materialQuantity_current(self):
        claimMaterialList_materialQuantity = super().get_data('$.lossInfo.claimMaterialList[*].materialQuantity.currentSubmitValue')
        return 'claimMaterialList_materialQuantity_current = '+str(claimMaterialList_materialQuantity)

    def claimMaterialList_materialQuantity_firstComplete(self):
        claimMaterialList_materialQuantity = super().get_data('$.lossInfo.claimMaterialList[*].materialQuantity.firstVersionEstReiCompleteValue')
        return 'claimMaterialList_materialQuantity_firstComplete = '+str(claimMaterialList_materialQuantity)
    
    def claimMaterialList_manualFlag(self):
        claimMaterialList_manualFlag = super().get_data('$.lossInfo.claimMaterialList[*].manualFlag')
        return 'claimMaterialList_manualFlag = '+str(claimMaterialList_manualFlag)
    
    def claimMaterialList_manualMatchedMaterial(self):
        claimMaterialList_manualMatchedMaterial = super().get_data('$.lossInfo.claimMaterialList[*].manualMatchedMaterial')        
        return 'claimMaterialList_manualMatchedMaterial = '+str(claimMaterialList_manualMatchedMaterial)
    
    def manualMatchedMaterial_materialCode(self):
        manualMatchedMaterial_materialCode = super().get_data('$.lossInfo.claimMaterialList[*].manualMatchedMaterial.materialCode')
        return 'manualMatchedMaterial_materialCode = '+str(manualMatchedMaterial_materialCode)
    
    def manualMatchedMaterial_materialName(self):
        manualMatchedMaterial_materialName = super().get_data('$.lossInfo.claimMaterialList[*].manualMatchedMaterial.materialName')
        return 'manualMatchedMaterial_materialName = '+str(manualMatchedMaterial_materialName)
    
    def claimMaterialList_materialTotalAmount_current(self):
        claimMaterialList_materialTotalAmount = super().get_data('$.lossInfo.claimMaterialList[*].materialTotalAmount.currentSubmitValue')
        return 'claimMaterialList_materialTotalAmount_current = '+str(claimMaterialList_materialTotalAmount)
    
    def claimMaterialList_materialTotalAmount_firstComplete(self):
        claimMaterialList_materialTotalAmount = super().get_data('$.lossInfo.claimMaterialList[*].materialTotalAmount.firstVersionEstReiCompleteValue')
        return 'claimMaterialList_materialTotalAmount_firstComplete = '+str(claimMaterialList_materialTotalAmount)
    
    def materialAmt_current(self):
        materialAmt = super().get_data('$.feeInfo.materialAmt.currentSubmitValue')
        return 'materialAmt_current = '+str(materialAmt)
    
    def materialAmt_firstComplete(self):
        materialAmt = super().get_data('$.feeInfo.materialAmt.firstVersionEstReiCompleteValue')
        return 'materialAmt_firstComplete = '+str(materialAmt)

    def estItemCnt_current(self):
        estItemCnt_current = super().get_data('$.lossInfo.estItemCnt.currentSubmitValue')
        return 'estItemCnt_current = '+str(estItemCnt_current)
    
    def estItemCnt_firstComplete(self):
        '''
        首次定核损结束时损失项目总量
        '''
        estItemCnt_first = super().get_data('$.lossInfo.estItemCnt.firstVersionEstReiCompleteValue')
        return 'estItemCnt_firstComplete = '+str(estItemCnt_first)

class rule(get_data):
    def __init__(self, claim_no):
        super().__init__(claim_no)

    def rule_0107010026(self):
        # get_data = self.get_data(claim_no)
        versionType = super().versionType()
        claimVersion = super().claim_version()
        vehicleHash_current = super().vehicleHash_current()
        vehicleHash_first = super().vehicleHash_firstComplete()
        laborAmt_first = super().laborAmt_firstComplete()
        laborAmt_current = super().laborAmt_current()
        return versionType,claimVersion,vehicleHash_current,vehicleHash_first,laborAmt_first,laborAmt_current

    def rule_0107010027(self):
        versionType = super().versionType()
        claimVersion = super().claim_version()
        repairFactoryType_current = super().repairFactoryType_current()
        repairFactoryType_firstComplete = super().repairFactoryType_firstComplete()
        vehicleHash_current = super().vehicleHash_current()
        vehicleHash_firstComplete = super().vehicleHash_firstComplete()
        claimPartList_manualFlag = super().claimPartList_manualFlag()
        claimPartList_partName = super().claimPartList_partName()
        claimPartList_standPartId = super().claimPartList_standardPartId()
        manualMatchedUniquePart_partName = super().manualMatchedUniquePart_partName()
        manualMatchedUniquePart_standPartId = super().manualMatchedUniquePart_standardId()
        partFeeDiscount_current = super().claimPartList_partFeeDiscount_current()
        partFeeDiscount_first = super().claimPartList_partFeeDiscount_firstComplete()
        repairFeeDiscount_current = super().claimPartList_repairFeeDiscount_current()
        repairFeeDiscount_first = super().claimPartList_repairFeeDiscount_firstComplete()
        paintFeeDiscount_current = super().claimPartList_paintFeeDiscount_current()
        paintFeeDiscount_first = super().claimPartList_paintFeeDiscount_firstComplete()
        removeFeeDiscount_current = super().claimPartList_removeFeeDiscount_current()
        removeFeeDiscount_first = super().claimPartList_removeFeeDiscount_firstComplete()
        return versionType,claimVersion,repairFactoryType_current,repairFactoryType_firstComplete,vehicleHash_current,\
                vehicleHash_firstComplete,claimPartList_manualFlag,claimPartList_partName,claimPartList_standPartId,\
                manualMatchedUniquePart_partName,manualMatchedUniquePart_standPartId,partFeeDiscount_current,\
                partFeeDiscount_first,repairFeeDiscount_current,repairFeeDiscount_first,paintFeeDiscount_current,\
                paintFeeDiscount_first,removeFeeDiscount_current,removeFeeDiscount_first

    def rule_0107010028(self):
        materialTotalAmount_current = super().claimMaterialList_materialTotalAmount_current()
        materialTotalAmount_first = super().claimMaterialList_materialTotalAmount_firstComplete()
        return materialTotalAmount_current,materialTotalAmount_first
    
    def rule_0107010029(self):
        claimMaterialList_materialQuantity_current = super().claimMaterialList_materialQuantity_current()
        claimMaterialList_materialQuantity_first = super().claimMaterialList_materialQuantity_firstComplete()
        materialTotalAmount_current = super().claimMaterialList_materialTotalAmount_current()
        materialTotalAmount_first = super().claimMaterialList_materialTotalAmount_firstComplete()
        return claimMaterialList_materialQuantity_current,claimMaterialList_materialQuantity_first,materialTotalAmount_current,materialTotalAmount_first        

    def rule_0107010030(self):
        materialAmt_firstComplete = super().materialAmt_firstComplete()
        materialAmt_current = super().materialAmt_current()
        return materialAmt_firstComplete,materialAmt_current
    
    def rule_0107010031(self):
        # part_name = super().claimPartList_partName()
        unitPriceDiscount_current = super().claimPartList_unitPriceDiscount_current()
        unitPriceDiscount_last = super().claimPartList_unitPriceDiscount_last()
        partType_current = super().claimPartList_part_current()
        partType_last = super().claimPartList_part_last()
        return unitPriceDiscount_current,unitPriceDiscount_last,partType_current,partType_last


if __name__ == '__main__':
    claim_no = 'acc_20210408_002'
    rule = rule(claim_no)
    rule_data = rule.rule_0107010031()
    for i in range(len(rule_data)):
        print(rule_data[i])