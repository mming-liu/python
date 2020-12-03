# -*- coding:utf-8 -*-
import os

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                file = file.split('.mp4')[0]
                L.append(os.path.join(file))
    return L

if __name__ == '__main__':
    links = ['https://www.zhihu.com/zvideo/1314159936125984768', 'https://www.zhihu.com/zvideo/1313606491677843456', 'https://www.zhihu.com/zvideo/1313247052558823424', 'https://www.zhihu.com/zvideo/1313246094068056064', 'https://www.zhihu.com/zvideo/1313245766828716032', 'https://www.zhihu.com/zvideo/1313245537194508288', 'https://www.zhihu.com/zvideo/1313245058301267968', 'https://www.zhihu.com/zvideo/1313244530867699713', 'https://www.zhihu.com/zvideo/1313243926669389824', 'https://www.zhihu.com/zvideo/1313243145501859840', 'https://www.zhihu.com/zvideo/1312812096644812800', 'https://www.zhihu.com/zvideo/1312809952978337792', 'https://www.zhihu.com/zvideo/1312518695705735168', 'https://www.zhihu.com/zvideo/1312518901301829632', 'https://www.zhihu.com/zvideo/1312518448149094400', 'https://www.zhihu.com/zvideo/1312518649446637568', 'https://www.zhihu.com/zvideo/1312516775066570752', 'https://www.zhihu.com/zvideo/1312517521363312640', 'https://www.zhihu.com/zvideo/1312517672547012608', 'https://www.zhihu.com/zvideo/1312515982083362816', 'https://www.zhihu.com/zvideo/1312517542288879616', 'https://www.zhihu.com/zvideo/1310605199539597312', 'https://www.zhihu.com/zvideo/1310604926696513536', 'https://www.zhihu.com/zvideo/1310604125378805760', 'https://www.zhihu.com/zvideo/1309562718597414912', 'https://www.zhihu.com/zvideo/1309428318463791104', 'https://www.zhihu.com/zvideo/1309086958929072128', 'https://www.zhihu.com/zvideo/1308805771892039680', 'https://www.zhihu.com/zvideo/1308529309117247488', 'https://www.zhihu.com/zvideo/1308528584755912704', 'https://www.zhihu.com/zvideo/1308525270736232448', 'https://www.zhihu.com/zvideo/1308524161665658880', 'https://www.zhihu.com/zvideo/1307806682979475456', 'https://www.zhihu.com/zvideo/1307078504333758464', 'https://www.zhihu.com/zvideo/1307078122026692608', 'https://www.zhihu.com/zvideo/1307077834595217408', 'https://www.zhihu.com/zvideo/1307077422378684416', 'https://www.zhihu.com/zvideo/1307077155269050368', 'https://www.zhihu.com/zvideo/1307076604041412608', 'https://www.zhihu.com/zvideo/1306918551451119616', 'https://www.zhihu.com/zvideo/1306918132612268032', 'https://www.zhihu.com/zvideo/1306911475450712064', 'https://www.zhihu.com/zvideo/1306696034014879744', 'https://www.zhihu.com/zvideo/1306695767449440256', 'https://www.zhihu.com/zvideo/1306695518961905664', 'https://www.zhihu.com/zvideo/1306693025268355072', 'https://www.zhihu.com/zvideo/1306688832994263040', 'https://www.zhihu.com/zvideo/1306556021767610368', 'https://www.zhihu.com/zvideo/1306555825322508288', 'https://www.zhihu.com/zvideo/1306555608217247744', 'https://www.zhihu.com/zvideo/1306282266658611200', 'https://www.zhihu.com/zvideo/1306282120264667136', 'https://www.zhihu.com/zvideo/1306281913548767232', 'https://www.zhihu.com/zvideo/1306281752588132352', 'https://www.zhihu.com/zvideo/1306281565299527680', 'https://www.zhihu.com/zvideo/1305062851674361856', 'https://www.zhihu.com/zvideo/1305055388862103552', 'https://www.zhihu.com/zvideo/1304711798566535168', 'https://www.zhihu.com/zvideo/1303994719018242048', 'https://www.zhihu.com/zvideo/1303994549534969856', 'https://www.zhihu.com/zvideo/1303994407876620288', 'https://www.zhihu.com/zvideo/1303994207209222144', 'https://www.zhihu.com/zvideo/1303993954937851904', 'https://www.zhihu.com/zvideo/1303993823371522048', 'https://www.zhihu.com/zvideo/1303993494420381696', 'https://www.zhihu.com/zvideo/1303685304537264128', 'https://www.zhihu.com/zvideo/1303685215722696704', 'https://www.zhihu.com/zvideo/1303685042787508224', 'https://www.zhihu.com/zvideo/1303684883919740928', 'https://www.zhihu.com/zvideo/1303684775723757568', 'https://www.zhihu.com/zvideo/1303684474434367488', 'https://www.zhihu.com/zvideo/1303684028063608832', 'https://www.zhihu.com/zvideo/1303683809334923264', 'https://www.zhihu.com/zvideo/1303683535975424000', 'https://www.zhihu.com/zvideo/1302359665703817216', 'https://www.zhihu.com/zvideo/1302358681682997248', 'https://www.zhihu.com/zvideo/1303096284149653504', 'https://www.zhihu.com/zvideo/1302710529073610752', 'https://www.zhihu.com/zvideo/1301996877731504128', 'https://www.zhihu.com/zvideo/1302710316426231808', 'https://www.zhihu.com/zvideo/1302710010787479552', 'https://www.zhihu.com/zvideo/1302359346387218432', 'https://www.zhihu.com/zvideo/1301947673126785024', 'https://www.zhihu.com/zvideo/1302359172973596672', 'https://www.zhihu.com/zvideo/1302354850274119680', 'https://www.zhihu.com/zvideo/1302318826886377472', 'https://www.zhihu.com/zvideo/1301918268941205504', 'https://www.zhihu.com/zvideo/1301949375774789632', 'https://www.zhihu.com/zvideo/1301914052591702016', 'https://www.zhihu.com/zvideo/1300205070705721344', 'https://www.zhihu.com/zvideo/1299824393741762560', 'https://www.zhihu.com/zvideo/1299820229460254720', 'https://www.zhihu.com/zvideo/1299623103145144320', 'https://www.zhihu.com/zvideo/1299085685098217472', 'https://www.zhihu.com/zvideo/1299083641957085184', 'https://www.zhihu.com/zvideo/1298957377551941632', 'https://www.zhihu.com/zvideo/1298938249847799808', 'https://www.zhihu.com/zvideo/1298935603271319552', 'https://www.zhihu.com/zvideo/1298715299315912704', 'https://www.zhihu.com/zvideo/1298714279575511040', 'https://www.zhihu.com/zvideo/1298713524395462656', 'https://www.zhihu.com/zvideo/1298712538691747840', 'https://www.zhihu.com/zvideo/1298711386583470080', 'https://www.zhihu.com/zvideo/1298376218878427136', 'https://www.zhihu.com/zvideo/1298257547049512960', 'https://www.zhihu.com/zvideo/1298027748921577472', 'https://www.zhihu.com/zvideo/1298027522869731328', 'https://www.zhihu.com/zvideo/1298027256514744320', 'https://www.zhihu.com/zvideo/1298027101506052096', 'https://www.zhihu.com/zvideo/1298026923810480128', 'https://www.zhihu.com/zvideo/1297662853281812480', 'https://www.zhihu.com/zvideo/1297657287851155456', 'https://www.zhihu.com/zvideo/1297592223681769472', 'https://www.zhihu.com/zvideo/1297592148595441664', 'https://www.zhihu.com/zvideo/1297592057322844160', 'https://www.zhihu.com/zvideo/1297511341394178048', 'https://www.zhihu.com/zvideo/1297501210510008320', 'https://www.zhihu.com/zvideo/1296931668998475776', 'https://www.zhihu.com/zvideo/1296927839238103040', 'https://www.zhihu.com/zvideo/1296810718223147008', 'https://www.zhihu.com/zvideo/1296798268999929856', 'https://www.zhihu.com/zvideo/1296759493469114368', 'https://www.zhihu.com/zvideo/1296755310405898240', 'https://www.zhihu.com/zvideo/1294671879169650688', 'https://www.zhihu.com/zvideo/1294669706209681408', 'https://www.zhihu.com/zvideo/1294665981907324928', 'https://www.zhihu.com/zvideo/1294617395999784960', 'https://www.zhihu.com/zvideo/1294614068636880896', 'https://www.zhihu.com/zvideo/1294612408280227840', 'https://www.zhihu.com/zvideo/1292531909441204224', 'https://www.zhihu.com/zvideo/1292528145837211648', 'https://www.zhihu.com/zvideo/1292451881818697728', 'https://www.zhihu.com/zvideo/1292447481431531520', 'https://www.zhihu.com/zvideo/1290086364768239616', 'https://www.zhihu.com/zvideo/1288740184607686656', 'https://www.zhihu.com/zvideo/1288482499069411328', 'https://www.zhihu.com/zvideo/1286934911706537984', 'https://www.zhihu.com/zvideo/1286289749930446848', 'https://www.zhihu.com/zvideo/1286218247591620608', 'https://www.zhihu.com/zvideo/1285129214505476096', 'https://www.zhihu.com/zvideo/1283751462380298240', 'https://www.zhihu.com/zvideo/1283052580789432320', 'https://www.zhihu.com/zvideo/1281146813995872256', 'https://www.zhihu.com/zvideo/1280998981808185344', 'https://www.zhihu.com/zvideo/1279005232635023360', 'https://www.zhihu.com/zvideo/1278650768753262592', 'https://www.zhihu.com/zvideo/1278640702310494208', 'https://www.zhihu.com/zvideo/1277234693411926016', 'https://www.zhihu.com/zvideo/1277234112622067712', 'https://www.zhihu.com/zvideo/1277233980752527360', 'https://www.zhihu.com/zvideo/1277233663303458816', 'https://www.zhihu.com/zvideo/1277232346761621504', 'https://www.zhihu.com/zvideo/1276799727225704448', 'https://www.zhihu.com/zvideo/1275826655785783296', 'https://www.zhihu.com/zvideo/1275563954623467520', 'https://www.zhihu.com/zvideo/1274806496400953344', 'https://www.zhihu.com/zvideo/1274797200338178048', 'https://www.zhihu.com/zvideo/1273907539042848768', 'https://www.zhihu.com/zvideo/1273204442880643072', 'https://www.zhihu.com/zvideo/1273204340090781696', 'https://www.zhihu.com/zvideo/1273172374670802944', 'https://www.zhihu.com/zvideo/1272796410346659840', 'https://www.zhihu.com/zvideo/1270850696288591872', 'https://www.zhihu.com/zvideo/1270372712935231488', 'https://www.zhihu.com/zvideo/1270367033335975936', 'https://www.zhihu.com/zvideo/1270362611926519808', 'https://www.zhihu.com/zvideo/1270339449843949568', 'https://www.zhihu.com/zvideo/1270338198213476352', 'https://www.zhihu.com/zvideo/1270337728212123648', 'https://www.zhihu.com/zvideo/1270337049397231616', 'https://www.zhihu.com/zvideo/1270333513024065536', 'https://www.zhihu.com/zvideo/1269337668284264448', 'https://www.zhihu.com/zvideo/1269249012848635904', 'https://www.zhihu.com/zvideo/1269205277296742400', 'https://www.zhihu.com/zvideo/1268886343334940672', 'https://www.zhihu.com/zvideo/1268880297484804096', 'https://www.zhihu.com/zvideo/1268679344849100800', 'https://www.zhihu.com/zvideo/1268536114316980224', 'https://www.zhihu.com/zvideo/1268530632771903488', 'https://www.zhihu.com/zvideo/1267399691324518400', 'https://www.zhihu.com/zvideo/1265989443296755712', 'https://www.zhihu.com/zvideo/1265925974090280960', 'https://www.zhihu.com/zvideo/1265711918608211968', 'https://www.zhihu.com/zvideo/1265711769727057920', 'https://www.zhihu.com/zvideo/1264249451260473344', 'https://www.zhihu.com/zvideo/1264240911925723136', 'https://www.zhihu.com/zvideo/1264235366426804224', 'https://www.zhihu.com/zvideo/1263841353052041216', 'https://www.zhihu.com/zvideo/1263838811160457216', 'https://www.zhihu.com/zvideo/1262715461601038336', 'https://www.zhihu.com/zvideo/1262491324495802368', 'https://www.zhihu.com/zvideo/1262334664984875008', 'https://www.zhihu.com/zvideo/1262325594467332096', 'https://www.zhihu.com/zvideo/1262004603811614720', 'https://www.zhihu.com/zvideo/1261634265105817600', 'https://www.zhihu.com/zvideo/1261628631162011648', 'https://www.zhihu.com/zvideo/1261625378801815552', 'https://www.zhihu.com/zvideo/1261280193152126976', 'https://www.zhihu.com/zvideo/1261276760555257856', 'https://www.zhihu.com/zvideo/1261271781677109248', 'https://www.zhihu.com/zvideo/1261267129765863424', 'https://www.zhihu.com/zvideo/1260638730131214336', 'https://www.zhihu.com/zvideo/1260635741883252736', 'https://www.zhihu.com/zvideo/1260632408040681472', 'https://www.zhihu.com/zvideo/1260343080534405120', 'https://www.zhihu.com/zvideo/1260190647564238848', 'https://www.zhihu.com/zvideo/1260188372250505216', 'https://www.zhihu.com/zvideo/1258519874927783936', 'https://www.zhihu.com/zvideo/1258143132828880896', 'https://www.zhihu.com/zvideo/1258129273446875136', 'https://www.zhihu.com/zvideo/1258122105537163264', 'https://www.zhihu.com/zvideo/1258116114590392320', 'https://www.zhihu.com/zvideo/1257345786322489344', 'https://www.zhihu.com/zvideo/1256846723118071808', 'https://www.zhihu.com/zvideo/1256482002335281152', 'https://www.zhihu.com/zvideo/1256479157514977280', 'https://www.zhihu.com/zvideo/1256123142688673792', 'https://www.zhihu.com/zvideo/1255467043577016320', 'https://www.zhihu.com/zvideo/1254730913655271424', 'https://www.zhihu.com/zvideo/1254715546656120832', 'https://www.zhihu.com/zvideo/1254307313231958016', 'https://www.zhihu.com/zvideo/1251985218246266880', 'https://www.zhihu.com/zvideo/1251052633030017024', 'https://www.zhihu.com/zvideo/1250558033132470272', 'https://www.zhihu.com/zvideo/1250380545990479872', 'https://www.zhihu.com/zvideo/1250189706894917632', 'https://www.zhihu.com/zvideo/1249219256057180160', 'https://www.zhihu.com/zvideo/1249203316501938176', 'https://www.zhihu.com/zvideo/1248876300388954112', 'https://www.zhihu.com/zvideo/1248378853451706368', 'https://www.zhihu.com/zvideo/1248331978324967424', 'https://www.zhihu.com/zvideo/1248145135197589504', 'https://www.zhihu.com/zvideo/1247226493320994816', 'https://www.zhihu.com/zvideo/1247190430435135488', 'https://www.zhihu.com/zvideo/1246907531576406016', 'https://www.zhihu.com/zvideo/1246907380585639936', 'https://www.zhihu.com/zvideo/1246210834923106304', 'https://www.zhihu.com/zvideo/1245431783123701760', 'https://www.zhihu.com/zvideo/1245387378468388864', 'https://www.zhihu.com/zvideo/1245318304149348352', 'https://www.zhihu.com/zvideo/1244699724407730176', 'https://www.zhihu.com/zvideo/1244612453448404992', 'https://www.zhihu.com/zvideo/1243635746760052736', 'https://www.zhihu.com/zvideo/1242586520357466112', 'https://www.zhihu.com/zvideo/1241250600056463360', 'https://www.zhihu.com/zvideo/1239071329577144320', 'https://www.zhihu.com/zvideo/1238728936416153600', 'https://www.zhihu.com/zvideo/1238724021711007744', 'https://www.zhihu.com/zvideo/1238365600952672256', 'https://www.zhihu.com/zvideo/1238360075960004608', 'https://www.zhihu.com/zvideo/1232713316067651584', 'https://www.zhihu.com/zvideo/1232712753112502272', 'https://www.zhihu.com/zvideo/1232712626678624256', 'https://www.zhihu.com/zvideo/1232712492976717824', 'https://www.zhihu.com/zvideo/1231261047975047168', 'https://www.zhihu.com/zvideo/1226264444848070656', 'https://www.zhihu.com/zvideo/1226251995834970112', 'https://www.zhihu.com/zvideo/1223608451072708608', 'https://www.zhihu.com/zvideo/1223269149176537088', 'https://www.zhihu.com/zvideo/1223264645475311616', 'https://www.zhihu.com/zvideo/1222217750816681984', 'https://www.zhihu.com/zvideo/1221204453963214848', 'https://www.zhihu.com/zvideo/1221181034769113088', 'https://www.zhihu.com/zvideo/1221176521924354048', 'https://www.zhihu.com/zvideo/1220312138071441408', 'https://www.zhihu.com/zvideo/1219611271122960384', 'https://www.zhihu.com/zvideo/1219611104323710976', 'https://www.zhihu.com/zvideo/1219291177356476416', 'https://www.zhihu.com/zvideo/1219290544653922304', 'https://www.zhihu.com/zvideo/1219289598133870592', 'https://www.zhihu.com/zvideo/1219288982766456832', 'https://www.zhihu.com/zvideo/1219288848808816640', 'https://www.zhihu.com/zvideo/1219288794421243904', 'https://www.zhihu.com/zvideo/1219288628993912832', 'https://www.zhihu.com/zvideo/1218613935127326720', 'https://www.zhihu.com/zvideo/1218295611826573312', 'https://www.zhihu.com/zvideo/1217566407707189248', 'https://www.zhihu.com/zvideo/1217558825165156352', 'https://www.zhihu.com/zvideo/1217488874068545536', 'https://www.zhihu.com/zvideo/1217459495607443456', 'https://www.zhihu.com/zvideo/1217456742957023232', 'https://www.zhihu.com/zvideo/1217162830476148736', 'https://www.zhihu.com/zvideo/1217162167394611200', 'https://www.zhihu.com/zvideo/1216861145719787520', 'https://www.zhihu.com/zvideo/1216861060101586944', 'https://www.zhihu.com/zvideo/1216837317048266752', 'https://www.zhihu.com/zvideo/1216833572805529600', 'https://www.zhihu.com/zvideo/1216833442832715776', 'https://www.zhihu.com/zvideo/1215918164712034304', 'https://www.zhihu.com/zvideo/1215401698476515328', 'https://www.zhihu.com/zvideo/1215237673327443968', 'https://www.zhihu.com/zvideo/1214676086744793088', 'https://www.zhihu.com/zvideo/1214305274145779712', 'https://www.zhihu.com/zvideo/1214202368725950464', 'https://www.zhihu.com/zvideo/1214153173117845504', 'https://www.zhihu.com/zvideo/1214146075655106560', 'https://www.zhihu.com/zvideo/1214140838978236416', 'https://www.zhihu.com/zvideo/1213944711871848448', 'https://www.zhihu.com/zvideo/1213940829167063040', 'https://www.zhihu.com/zvideo/1213539452729401344', 'https://www.zhihu.com/zvideo/1213519850175385600', 'https://www.zhihu.com/zvideo/1213519284083101696', 'https://www.zhihu.com/zvideo/1213380041943461888', 'https://www.zhihu.com/zvideo/1213152444496363520', 'https://www.zhihu.com/zvideo/1213145479569096704', 'https://www.zhihu.com/zvideo/1212656788329533440', 'https://www.zhihu.com/zvideo/1212449452159664128', 'https://www.zhihu.com/zvideo/1212101810082766848', 'https://www.zhihu.com/zvideo/1212099202891079680', 'https://www.zhihu.com/zvideo/1211042934008885248', 'https://www.zhihu.com/zvideo/1210661618163642368', 'https://www.zhihu.com/zvideo/1210651764095266816', 'https://www.zhihu.com/zvideo/1210479364422496256', 'https://www.zhihu.com/zvideo/1210315797815873536', 'https://www.zhihu.com/zvideo/1210310160931139584', 'https://www.zhihu.com/zvideo/1210306774676570112', 'https://www.zhihu.com/zvideo/1209580457018437632', 'https://www.zhihu.com/zvideo/1209006918838292480', 'https://www.zhihu.com/zvideo/1208164186175709184', 'https://www.zhihu.com/zvideo/1208131103573508096', 'https://www.zhihu.com/zvideo/1207421008048693248', 'https://www.zhihu.com/zvideo/1206344862167330816', 'https://www.zhihu.com/zvideo/1205871521320861696', 'https://www.zhihu.com/zvideo/1205606452196634624', 'https://www.zhihu.com/zvideo/1205549674020700160', 'https://www.zhihu.com/zvideo/1204761466047627264', 'https://www.zhihu.com/zvideo/1204752293033562112', 'https://www.zhihu.com/zvideo/1204744961113169920', 'https://www.zhihu.com/zvideo/1204004612313071616', 'https://www.zhihu.com/zvideo/1203997796237484032', 'https://www.zhihu.com/zvideo/1203986196189347840', 'https://www.zhihu.com/zvideo/1203245109275668480', 'https://www.zhihu.com/zvideo/1202562659885064192', 'https://www.zhihu.com/zvideo/1201447302550036480', 'https://www.zhihu.com/zvideo/1201072477423673344', 'https://www.zhihu.com/zvideo/1200725231180189696', 'https://www.zhihu.com/zvideo/1199793149172035584', 'https://www.zhihu.com/zvideo/1199674311583367168', 'https://www.zhihu.com/zvideo/1199649588300427264', 'https://www.zhihu.com/zvideo/1199637762246402048', 'https://www.zhihu.com/zvideo/1199390015748542464', 'https://www.zhihu.com/zvideo/1199385321546362880', 'https://www.zhihu.com/zvideo/1199045328537776128', 'https://www.zhihu.com/zvideo/1198743608486322176', 'https://www.zhihu.com/zvideo/1198743319926472704', 'https://www.zhihu.com/zvideo/1198013985923244032', 'https://www.zhihu.com/zvideo/1197822896524124160', 'https://www.zhihu.com/zvideo/1197644046552698880', 'https://www.zhihu.com/zvideo/1197296005421621248', 'https://www.zhihu.com/zvideo/1196918605668098048', 'https://www.zhihu.com/zvideo/1196774025081565184', 'https://www.zhihu.com/zvideo/1196585288980443136', 'https://www.zhihu.com/zvideo/1196197560610648064', 'https://www.zhihu.com/zvideo/1195106128898674688', 'https://www.zhihu.com/zvideo/1195100622289219584', 'https://www.zhihu.com/zvideo/1194737934740336640', 'https://www.zhihu.com/zvideo/1194707268065828864', 'https://www.zhihu.com/zvideo/1194191300239511552', 'https://www.zhihu.com/zvideo/1194191000942379008', 'https://www.zhihu.com/zvideo/1194190739175985152', 'https://www.zhihu.com/zvideo/1190748143191441408', 'https://www.zhihu.com/zvideo/1190746934602977280', 'https://www.zhihu.com/zvideo/1190746513238917120', 'https://www.zhihu.com/zvideo/1190745656539627520', 'https://www.zhihu.com/zvideo/1190742161291980800']
    titles = ['50个行测小技巧：增长量大小比较', '山东省公务员考试：俯视图和左视图', '2019年山东省公务员考试资料分析', '2019年山东省公务员考试类比推理', '2019年山东省公务员考试图形推理', '2019年山东省公务员考试数量关系', '2019年山东省公务员考试篇章阅读', '2019年山东省公务员考试逻辑填空', '2019年山东省公务员考试逻辑判断', '2019年山东省公务员考试定义判断', '2019年山东省公务员考试：同余定理', '2019年山东省公务员考试：空瓶换酒问题', '2020年江苏公务员考试篇章阅读', '2020年江苏省公务员考试定义判断', '2020年江苏省公务员考试逻辑判断', '2020年江苏公务员考试资料分析', '2020年江苏省公务员考试类比推理', '2020年江苏省公务员考试图形推理', '2020年江苏省公务员考试数量关系', '2020江苏省公务员考试数字推理', '2020年江苏省公务员考试逻辑填空', '公务员考试：长方形花坛周长20米', '江苏省公务员考试：两位警官梳理案件', '江苏省公务员考试：某单位要抽调若干人员下乡扶贫', '公务员考试：资料分析别硬算，谁算谁完蛋！', '公务员考试：内核和硬核什么关系？', '公务员考试：常考逻辑错误之群体属性和个体属性的混淆', '公务员考试：6条直线最多将一个平面分成几部分？', '公务员考试：快递员取件成功的概率为？', '公务员考试：谷堆的高度为？', '公务员考试：长方形D的最大面积是？', '公务员考试：圆柱型容器的水面高度达到？', '公务员联考：速算技巧之溶液法', '50个行测小技巧：环排与错位重排', '50个行测小技巧：牛吃草问题', '50个行测小技巧：插板法', '50个行测小技巧：三集合容斥问题', '50个行测小技巧：多次相遇追及', '50个行测小技巧：整除特性', '50个行测小技巧：逻辑填空优选高端大气内涵丰富的词汇', '50个行测小技巧：逻辑填空看提示信息', '江苏省公务员考试：张某怎么死的？', '50个行测小技巧：空间图形推理路径法', '50个行测小技巧：空间图形推理公共点法', '50个行测小技巧：空间图形推理坐标法', '50个行测小技巧：空间图形推理时针法', '50个行测小技巧：空间图形推理相对面', '行测50个小技巧：平面图形推理观察选项法', '行测50个小技巧：一笔画图形的两种判定方式', '行测50个小技巧：平面图形推理三句口诀', '50个行测小技巧：等价排除原则', '50个行测小技巧：择优原则', '50个行测小技巧：跳坑原则', '50个行测小技巧：字面意思理解法', '50个行测小技巧：直选法', '2019年国家公务员考试逻辑填空', '2019年国家公务员考试类比推理', '公务员考试：将货物集中到哪个仓库运费最少呢？', '50个行测小技巧：推出型论证', '50个行测小技巧：对比实验论证', '50个行测小技巧：推测类论证', '50个行测小技巧：因果论证的加强', '50个行测小技巧：等价排除原则', '50个行测小技巧：确定信息破题', '50个行测小技巧：最大信息破题', '50个行测小技巧：排除法优先', '50个行测小技巧：模态命题', '50个行测小技巧：真假推理中的推出关系', '50个行测小技巧：真假推理中的反对关系', '50个行测小技巧：真假推理中的矛盾命题', '50个行测小技巧：从弱原则', '50个行测小技巧：鲁滨逊定理', '50个行测小技巧：翻译推理并列关系', '50个行测小技巧：翻译推理中的推出关系', '50个行测小技巧：基期比重和基期差的快捷计算', '50个行测小技巧：反向代入法', '公务员考试：一道让人啧啧称奇的真假推理题', '50个行测小技巧：增长率的快捷计算', '50个行测小技巧：化除为乘', '50个行测小技巧：比重差公式的妙用', '50个行测小技巧：年均增长率与二项式定理', '50个行测小技巧：插值法', '50个行测小技巧：百化分', '50个行测小技巧：尾数法', '关于Y原子的这个公务员考试题，实际上没答案', '北京公务员考试：兰兰、晶晶、玲玲谁得了100分？', '50个行测小技巧：基本乘除技巧', '50个行测小技巧：溶液法', '50个行测小技巧：凑整平衡思想', '公务员考试：资料分析速算中的凑整思想', '表弟问我：企业年薪十二万VS公务员月薪五千，选哪个？', '国家公务员考试：如何快速找到最适合自己的岗位？', '公务员考试：关于叶龄指数的说法', '国家公务员考试：空间图形推理，2016年第75题', '国家公务员考试：这题居然两个答案！', '公务员考试：有一位百岁老人出生于二十世纪', '公务员考试：A公司希望完成全年的销售任务', '公务员考试：不同参赛顺序的种数在以下哪个范围之内？', '2017国家公务员考试：空间图形推理76题', '公务员考试：甲部门每隔2天、乙部门每隔3天', '公务员考试：最适合做这段文字标题的是？', '公务员考试：废寝忘食和呕心沥血有什么不同？', '公务员考试：指责、批评和谴责有什么区别？', '公务员考试：哪个图能反映Y的上、下限和X的关系？', '公务员考试：正确率只有30%的题目，你能做对吗？', '公务员考试：素描是种单色绘画', '公务员考试：昼夜交替是因为什么？', '公务员考试：自然科学和化学什么关系？', '公务员考试：教、学和教学', '公务员考试：佩刀和刀鞘什么关系？', '2017年国家公务员考试逻辑判断', '2017年国家公务员考试资料分析', '国家公务员考试：踢皮球和互相推诿什么关系？3', '公务员考试：寒、寒冷、寒舍什么关系？', '公务员考试：白醋和消毒是什么关系？', '江苏公务员考试：四个图形可以拼接成哪个图形？', '这两道题华图和粉笔答案不一样，我站华图，你呢？', '2017年国家公务员考试定义判断', '2017年国家公务员考试图形推理', '国家公务员考试：购买白糖花了多少钱？', '国家公务员考试：种植白色花卉的区域占总面积的多少？', '国家公务员考试：赵某未选择丙类题的概率为多少', '国家公务员考试：某人的年龄等于当年年份数字之和', '国家公务员考试：这个三个数谁最大？谁最小？mp4', '国家公务员考试：跨期增长率的应用，很多同学都不会', '国家公务员考试：哪位运动员体能测试没达标？', '国家公务员考试真题：幼年时期听话的孩子可能缺乏创造力', '国家公务员考试真题：飞禽走兽和大雁、海鸥什么关系？', '国家公务员考试真题：蛋、卤蛋和松花蛋是什么关系？', '2018国考篇章阅读', '国家公务员考试真题：如何使得有效票数最多？', '国家公务员考试：小张和小李坐在同一排的概率是多少？', '这题答案改过来改过去，到底选哪个呢？', '2018国考逻辑填空', '公务员考试：温度决定了绿海龟孵化时的性别', '粉笔科技CEO张小龙怒批湖南卫视扶贫节目造假，沈梦辰刷大牌', '2019国考快速比较大小', '2019国考逻辑判断', '江苏省公务员考试真题：减肥，管住嘴比迈开腿更重要', '2020年8月份热点公务员面试真题讲解及点评', '2019国考定义判断', '几乎不动笔，解决北京公务员考试资料分析真题', '公务员考试：如何算出这道题？', '猫哥公务员事业编面试线上课录播节选8月23日', '国家公务员考试真题：你能把这六个图形分为两组吗？', '2019国考数量关系', '2019年国家公务员考试：摆成实心矩形，最外层最少有多少盆花', '关于公考面试班', '猫哥的公考面试小册子', '公考面试中那些常见的错误', '公考面试如何拿高分', '猫哥的公考面试概述', '一天，三个逻辑学家走进了一家酒馆', '容易把人绕晕的公务员考试题', '公务员考试：如何又快又准的算出这道题？', '公务员考试：如何用眼瞪出这道题？', '2019年国家公务员考试真题：甲车上午8点从A地出发匀速开往', '山东省公务员考试：如何更快算出这个题', '资料分析技巧日常分享：比较大小', '资料分析日常分享', '资料分析不分析，提笔就算！这是大部分行测不到70的同学的通病', '如何瞪出这道题？', '2020年7月25日多省公务员联考华图粉笔分歧题目探讨', '2020山东省考资料分析', '2020山东省考逻辑判断', '2020山东省考类比推理', '2020山东省考定义判断', '2020山东省考图形推理', '2020山东省考数量关系', '2020山东省考篇章阅读', '2020山东省考逻辑填空', '2020国考资料分析', '2020国考逻辑判断', '2020国考类比推理', '2020国考定义判断', '2020图形推理', '2020国考数量关系', '2020国考篇章阅读', '2020国考逻辑填空', '公务员考试：资料分析原来可以这么做？', '重庆公务员考试真题：增长量之比', '公务员考试：资料分析中基期比重和基期差的快捷计算', '公务员考试：资料分析中的一个重要估算公式', '公务员考试：资料分析中的误差控制总原则', '江苏公务员考试真题：三角形AEF与三角形CEF的面积之比是？', '上海公务员考试真题：蚂蚁从A到B的最短路径有多长？', '海南公务员考试真题：A到B的距离等于多少？', '重庆公务员考试真题：哪种方式散热快？', '江苏省公务员考试真题：关于水资源，下列说法正确的是', '2014年国家公务员考试：30个人围坐在一起轮流表演节目', '猫哥继续带你秒杀公务员考试空间图形推理', '公务员考试：结构化面试概述', '讲了个赋值法的经典题目，猫哥头又被锤爆了', '上海公务员考试真题：赋值法秒解三角形内角和问题', '公务员考试之等价排除原则：阅读名著', '公务员考试：正方体变长方体，表面积如何变化？', '公务员考试之整除特性：孩子到底出生在哪个月？', '国家公务员考试真题：请把六个银行的标志按照某种规律分为两组', '看到百分数、比例，就想到整除特性，是备考公务员的基本素质', '公务员考试：遮蔽和隐藏有什么区别？', '各位准公务员，家里台灯多少瓦，心里有数没？', '猫哥带你做行测：如何快又准得算出这道公务员考试题？', '猫哥带你做行测：这道公务员考试题，你要多少秒能算出来？', '看猫哥如何口算出这个公务员考试资料分析题', '猫哥带你做行测：盈亏思想秒解这道送鸡蛋的题', '22个球中有1个略重，最优方案下最多用几次天平可以找出来它？', '猫哥带你做行测：如何连蒙带猜地做对这道行程题', '猫哥带你做行测：桥牌比赛，小王和小李分在一组的概率是多少？', '猫哥带你做行测：分析大于计算之热气球两段速度之比', '猫哥带你做行测：盈亏思想解决分泥土的问题', '猫哥带你做行测：根据提示词，直接秒杀这道逻辑填空：一支奇葩', '溶液法解决这道题：马拉松赛事增速同比', '一道挺难的江苏事业单位真题，你需要多久能做出来？', '公务员考试：接语选择题，只需要把握这一个原则即可', '公考行测：企业办证工作人员效率提高', '公考行测：利用杠杆法快速求平均增长率', '公考行测：模态命题这么难吗？学生优惠12岁', '公务员考试：资料分析提笔就算？这毛病不改永远得不到高分！', '华图选A，粉笔选D，猫哥和中公选C，你选哪个？', '思路清奇的公务员考试真题：老张爸妈身体是真不错', '经典行测题目分享：冒充言语理解的逻辑', '猫哥带你做行测：2018年重庆公务员考试数量和判断推理', '公务员行测：学生和猫哥讨论了几道颇为棘手的问题', '资料分析提笔就算？猫哥严厉地批评了这个同学！', '30道空间图形推理，道道秒杀，猫哥不愧是专业判断推理老师！', '猫哥带你做行测：18重庆逻辑填空', '猫哥带你做行测：海盗猖獗与高额赎金', '猫哥带你做行测：正确率只有14%的逻辑题——用水超标家庭', '公务员考试：构造法求年均增长率', '公务员考试：隔板法经典例题', '公务员考试：不动笔解决资料分析之基期比重', '如何蒙对史上最难国考行测题？', '公考行测：超级麻烦的一道题，原来还可以这么解决', '言语理解中，主旨概括题与意图推断题的区别与联系', '行测80分大神教你如何摸透出题人的心思，秒杀资料分析', '反向代入法，猫哥讲一次被网友锤一次，但是真的好用', '猫哥的行测80分之路：类比推理', '集合推理，你画图解决就行了！', '这个比较大小还用算吗？资料分析，要分析啊，不要动笔就算', '公考行测：构造条件破解真假推理', '公考行测：反向代入思想的妙用', '公考行测：鲁宾逊公式', '增长率的72法则', '2020.5.9带学员分析他的言语理解错题', '2018陕西省考资料分析，行测技术不过硬，真的会崩溃啊', '行测80分之路：整数的因式分解', '行测80猫哥资料分析日常分享2', '行测80猫哥资料分析日常分享', '选项差距超过10%的资料分析基本都是送分题', '五次公考五进面的猫哥这样做资料分析', '行测75到80的猫哥指导70分以下的学生，差距一目了然', '10个西瓜，取若干个，有多少种取法？', '初中生会做大学生不会做的公务员考试题，你能选对吗？', '公考行测：你需要多少秒能算出这个式子？', '中药果真强大！', '行测想上80，这两种速算技巧必须掌握', '拆桥的削弱力度很强，仅次于直接削弱论点？猫哥有话说', '公考行测：猫哥悬赏100元，求高人指导3道逻辑判断', '公考行测：一个命题推出它的矛盾命题，说明什么？', '公考行测：快速计算乘法的一个小窍门', '这题绝了，华图选B，粉笔选C，中公选D，你选哪个？', '公考行测：一道争议题，机构选D，我选B，我信心十足，你选哪个', '公考行测：这道题目不简单，试试你几分钟能做出来？', '公考行测：小赵从家到单位，有多少路线可以选择？', '有同学问这道题有什么简便方法？很简答，插值法嘛', '我从未见过如此坑人的公务员考试真题', '山东的一道超级难的资料分析，你能几分钟做出来？', '行测80分之路：资料分析第十四讲——求和的几个简便方法', '行测80分之路：资料分析第十三讲——利用常识', '行测80分之路：资料分析第十二讲——插值法', '行测80分之路：资料分析第十一讲——选项反推法', '行测80分之路：资料分析第十讲——尾数法', '行测80分之路：资料分析第九讲——二项式定理求年均增长率', '行测80分之路：资料分析第八讲——十字交叉法求混合增长率', '行测80分大神带你秒解资料分析精确计算', '行测80分之路：资料分析不靠算，谁算谁完蛋！', '行测80分之路：资料分析第七讲——大小比较', '猫哥公考私塾班连麦答疑节选：求和的高位叠加法', '有同学说自己备考公务员很努力，光钱就花了好几万，我一巴掌', '公考行测：如何给文章起个好的标题', '公考行测：支持和推出有什么区别？', '行测80分之路：资料分析第六讲——专克除法计算的溶液法', '行测80分之路：资料分析第五讲——化除为乘及误差分析', '行测80分之路：资料分析第四讲——百化分及误差分析', '行测80分之路：资料分析第三讲——乘除5、9、11的技巧', '江苏省考的一道空间图形推理，这种正方体的都是送分题', '行测80分之路：资料分析第二讲——误差控制总原则', '行测80分之路：资料分析第一讲——基础知识', '公考行测：分母减8，分子得减多少，才能保持这个分式的值不变？', '资料分析：百化分的误差修正', '公考行测中第二好用的秒杀技巧：等价排除原则', '行测考试最实用的秒杀技巧，没有之一', '巧用常识解决资料分析中国家间的比较问题', '公考行测：如何巧用二项式定理求年均增长率', '2019年山东省考真题，溶液法的经典题目', '公考资料分析原则：计算误差一定要小于选项最小差距', '资料分析计算误差控制，遵循这个原则即可', '利用语气强弱巧解江苏省2020年公务员考试常识真题', '江苏2020年公务员考试真题：儿童校外生活满意重视', '每晚7点半，猫哥开始整理历年公务员考试真题，你愿意一起吗？', '公考行测：资料分析中，溶液法的使用误区', '公考行测：插板法解决多位数各个位上数字之和为定值的问题', '公考行测：翻译推理的一道经典题目，2017年山东省公务员考试', '公考行测：整数的多次幂尾数变化规律', '公考行测：资料分析中如何控制误差', '公考行测：资料分析中，如何用二项式定理求年均增长率？', '公考行测：一笔画图形，你还在数奇点吗？试试这个新方法吧', '公考行测：不动笔解决资料分析', '公考行测：不是吹，多数资料分析不动笔就能做出来，江苏省考为例', '网上哪里有免费的公务员考试历年真题呢？', '公考行测：如何几乎不动笔计算加权平均数？原来如此简单', '公考行测：资料分析，有同学算半天，看大神如何秒选答案', '1分钟内你能做出这道真题吗？看行测80分大神如何20秒解决', '吉林省公务员考试真题：下列没有歧义的一项是', '公务员考试真题：如果有人出身于60年代，那么他肯定读过', '公考行测：类比推理——白驹过隙：秒表', '公考行测：资料分析不进行计算，结合常识快速得到答案，妙啊', '公考行测：综合度超高的一道真假推理题，你能做对吗？', '如何选择公考笔试辅导班？我来说几句掏心窝子的话', '公考行测：资料分析中，选项十分接近，选哪个呢？', '考公务员有多难？相当于高考什么水平？', '2018年浙江省公务员考试122题：杠杆法求混合增长率的应用', '公考行测：资料分析中五年的平均增长量是差额除以4还是除以5？', '2014年山东省公务员考试的一道空间图形推理题', '公考行测：2020国考的一个排列组合题，正确率47%', '公考行测：资料分析中，选项很接近的年均增长率怎么求？', '公考行测：资料分析，选项差距很小，看80分行测高手如何搞定', '行测80分高手如何做资料分析，以本题为例', '公务员考试真题：厨师和炒鱿鱼什么关系？', '公考行测：一道著名的逻辑判断争议难题，你选哪个呢？', '你和小明掷骰子，你的点数大于他的概率是多少？', '没关系没背景别考公务员？请别把你的无知当做成熟', '公务员面试中常犯的致命失误，你知道几条？', '公务员面试中绝对不能犯的几种致命错误', '公务员月薪五千相当于私企月薪多少？不算不知道，一算吓一跳啊', '那些考上公务员之后才知道的坑', '还在为名言警句积累太少发愁吗？猫哥已经为你准备好了，速速领取', '公考行测：定义判断的几个小技巧', '备考公务员的过程中，如何面对争议题呢', '省考84分大作文原来是这样的啊，技巧一学就会！', '一页ppt搞定公考行测中的加强削弱题', '五次公考五进面的猫哥建议大家这样备考公务员', '公考行测：数量关系中的流水行船问题', '公务员真题日常答疑：狗的焦虑症和镁离子', '公考行测：排列组合问题必须掌握的几个知识点', '国考笔试成绩出炉，如何选择公务员面试辅导班呢？', '公务员考试真题，你能30秒选出答案吗？', '公务员成绩出来了，要不要报个面试辅导班？', '公考行测：数量关系中的抽屉原理（最不利原则）', '公考行测：多次相遇追及问题的几个重要结论', '数量关系中的牛吃草问题', '数量关系中的三集合容斥问题', '公考行测：数量关系中的整除特性', '利用数字的整除特性解数量关系', '线段法在混合增长率中的应用', '什么是恩格尔系数？什么是基尼系数？5分钟彻底明白', '公考行测：如何快速记住常见平方数？凑整法', '公考行测：给你3分钟，可以求出“？”处的面积吗？', '插板法：10个相同的糖果，分给3个小朋友，有多少种分法？', '经典行程问题', '公考行测判断推理之真假推理', '公考行测之空间图形推理', '加强削弱之提高篇', '加强削弱之基础篇', '公考行测判断推理之翻译推理']
    file_dir = 'D://批量下载视频/'

    video_names = file_name(file_dir)
    print(len(titles))
    print(len(video_names))
    print(video_names)
    print(sorted(titles))
    print(sorted(video_names))
    for m in titles :
        if m not in video_names:
            index = titles.index(m)
            print(video_names)
            print(links[index])