

def Dijkstra(G,start,end):    
    vNum = len(G)
    path = [start]
    calc = {}
    for key in G[start]:
        calc[key] = G[start][key]  
    while len(calc)>0:
        for key in calc:
            najkrace = calc[key]
            for moguce in G[key]:
                if( (calc[key]+G[key][moguce]) < najkrace ):
                    najkrace = calc[key]+G[key][moguce]            
            calc[key] = najkrace            
        node = min(calc, key=calc.get)
        path.append(node)
        del calc[node]
        if(node==end):
            break
    return path


#main
print "START"
coords = [[45.557986854,18.713400671],[45.557994366,18.710986682],[45.558283584,18.710772106],[45.557962439,18.708891877],[45.557862902,18.708492228],[45.557782146,18.708792635],[45.557273191,18.710745284],[45.556980211,18.712043473],[45.556108774,18.715680548],[45.557231873,18.715720781],[45.557983098,18.715793201],[45.558786896,18.715862938],[45.559624488,18.715954134],[45.560105252,18.715321132],[45.559819799,18.715133378],[45.560383192,18.715927311],[45.560916532,18.717901417],[45.560555965,18.719006487],[45.560345632,18.718883106],[45.560330609,18.718453952],[45.559808531,18.718207189],[45.559870504,18.718893835],[45.558863895,18.719151327],[45.558800043,18.717922875],[45.558766238,18.716941186],[45.557748341,18.717912146],[45.557973707,18.718593427],[45.557256288,18.716871449],[45.557320143,18.719381997],[45.556313488,18.719682404],[45.555002556,18.720256397],[45.555922841,18.716731974],[45.556099384,18.716839263]]
distance = [[0, '188', '227', '377', '412', '399', '271', '377', '395', '270', '186', '276', '373', '459', '500', '463', '630', '616', '591', '558', '496', '649', '534', '437', '361', '554', '579', '359', '556', '669', '777', '479', '488'], ['188', 0, '39', '189', '224', '211', '83', '189', '489', '614', '698', '788', '885', '971', '969', '975', '1142', '1128', '1103', '1070', '1008', '1161', '1046', '949', '873', '1066', '1091', '703', '900', '829', '871', '573', '594'], ['227', '39', 0, '151', '185', '173', '121', '227', '527', '652', '736', '826', '923', '1009', '930', '1013', '1180', '1166', '1141', '1108', '1046', '1199', '1084', '987', '911', '1104', '1129', '741', '938', '867', '909', '611', '632'], ['377', '189', '151', 0, '34', '22', '183', '290', '590', '715', '799', '889', '986', '1072', '779', '1076', '1243', '1229', '1204', '1171', '1109', '1262', '1147', '1050', '974', '1167', '1192', '804', '1001', '930', '972', '674', '695'], ['412', '224', '185', '34', 0, '27', '188', '295', '594', '719', '803', '893', '990', '1076', '745', '1080', '1247', '1233', '1208', '1175', '1113', '1266', '1151', '1054', '978', '1171', '1196', '808', '1005', '934', '976', '678', '699'], ['399', '211', '173', '22', '27', 0, '161', '268', '568', '693', '777', '867', '964', '1050', '771', '1054', '1221', '1207', '1182', '1149', '1087', '1240', '1125', '1028', '952', '1145', '1170', '782', '979', '908', '950', '652', '673'], ['271', '83', '121', '183', '188', '161', 0, '106', '406', '531', '615', '705', '802', '888', '933', '892', '1059', '1045', '1020', '987', '925', '1078', '963', '866', '790', '983', '1008', '620', '817', '746', '788', '490', '511'], ['377', '189', '227', '290', '295', '268', '106', 0, '300', '425', '509', '599', '696', '782', '823', '786', '953', '939', '914', '881', '819', '972', '857', '760', '684', '877', '902', '514', '711', '640', '682', '384', '405'], ['395', '489', '527', '590', '594', '568', '406', '300', 0, '125', '209', '299', '396', '482', '523', '486', '653', '639', '614', '581', '519', '672', '557', '460', '384', '577', '602', '214', '411', '340', '382', '84', '105'], ['270', '614', '652', '715', '719', '693', '531', '425', '125', 0, '84', '174', '271', '357', '398', '361', '528', '514', '489', '456', '394', '547', '432', '335', '257', '452', '477', '89', '286', '399', '507', '209', '218'], ['186', '698', '736', '799', '803', '777', '615', '509', '209', '84', 0, '90', '187', '273', '314', '277', '444', '430', '405', '372', '310', '463', '348', '251', '175', '368', '393', '173', '370', '483', '591', '293', '302'], ['276', '788', '826', '889', '893', '867', '705', '599', '299', '174', '90', 0, '97', '183', '224', '187', '354', '339', '314', '281', '219', '372', '257', '160', '84', '277', '302', '252', '431', '544', '681', '383', '381'], ['373', '885', '923', '986', '990', '964', '802', '696', '396', '271', '187', '97', 0, '85', '126', '90', '257', '283', '258', '226', '294', '311', '346', '249', '173', '366', '391', '341', '520', '633', '778', '480', '470'], ['459', '971', '1009', '1072', '1076', '1050', '888', '782', '482', '357', '273', '183', '85', 0, '41', '146', '313', '339', '314', '281', '343', '367', '431', '334', '258', '451', '476', '426', '605', '718', '863', '565', '555'], ['500', '969', '930', '779', '745', '771', '933', '823', '523', '398', '314', '224', '126', '41', 0, '187', '354', '380', '355', '322', '384', '408', '472', '375', '299', '492', '517', '467', '646', '759', '904', '606', '596'], ['463', '975', '1013', '1076', '1080', '1054', '892', '786', '486', '361', '277', '187', '90', '146', '187', 0, '166', '266', '308', '276', '338', '361', '436', '339', '263', '456', '481', '431', '650', '762', '868', '570', '560'], ['630', '1142', '1180', '1243', '1247', '1221', '1059', '953', '653', '528', '444', '354', '257', '313', '354', '166', 0, '100', '121', '154', '216', '174', '288', '385', '430', '502', '527', '598', '463', '575', '727', '737', '727'], ['616', '1128', '1166', '1229', '1233', '1207', '1045', '939', '639', '514', '430', '339', '283', '339', '380', '266', '100', 0, '25', '58', '120', '78', '192', '289', '365', '406', '431', '533', '367', '479', '631', '683', '662'], ['591', '1103', '1141', '1204', '1208', '1182', '1020', '914', '614', '489', '405', '314', '258', '314', '355', '308', '121', '25', 0, '33', '95', '53', '167', '264', '340', '381', '406', '508', '342', '454', '606', '658', '637'], ['558', '1070', '1108', '1171', '1175', '1149', '987', '881', '581', '456', '372', '281', '226', '281', '322', '276', '154', '58', '33', 0, '62', '86', '200', '297', '347', '414', '439', '515', '375', '487', '639', '665', '644'], ['496', '1008', '1046', '1109', '1113', '1087', '925', '819', '519', '394', '310', '219', '294', '343', '384', '338', '216', '120', '95', '62', 0, '148', '262', '361', '285', '478', '503', '453', '437', '549', '701', '603', '582'], ['649', '1161', '1199', '1262', '1266', '1240', '1078', '972', '672', '547', '463', '372', '311', '367', '408', '361', '174', '78', '53', '86', '148', 0, '115', '212', '288', '329', '354', '456', '289', '401', '553', '606', '585'], ['534', '1046', '1084', '1147', '1151', '1125', '963', '857', '557', '432', '348', '257', '346', '431', '472', '436', '288', '192', '167', '200', '262', '115', 0, '97', '173', '214', '239', '341', '174', '287', '439', '491', '470'], ['437', '949', '987', '1050', '1054', '1028', '866', '760', '460', '335', '251', '160', '249', '334', '375', '339', '385', '289', '264', '297', '361', '212', '97', 0, '76', '117', '142', '244', '271', '384', '536', '394', '373'], ['361', '873', '911', '974', '978', '952', '790', '684', '384', '257', '175', '84', '173', '258', '299', '263', '430', '365', '340', '347', '285', '288', '173', '76', 0, '193', '218', '168', '347', '460', '616', '318', '297'], ['554', '1066', '1104', '1167', '1171', '1145', '983', '877', '577', '452', '368', '277', '366', '451', '492', '456', '502', '406', '381', '414', '478', '329', '214', '117', '193', 0, '73', '361', '388', '501', '653', '511', '490'], ['579', '1091', '1129', '1192', '1196', '1170', '1008', '902', '602', '477', '393', '302', '391', '476', '517', '481', '527', '431', '406', '439', '503', '354', '239', '142', '218', '73', 0, '386', '413', '526', '678', '536', '515'], ['359', '703', '741', '804', '808', '782', '620', '514', '214', '89', '173', '252', '341', '426', '467', '431', '598', '533', '508', '515', '453', '456', '341', '244', '168', '361', '386', 0, '197', '310', '448', '150', '129'], ['556', '900', '938', '1001', '1005', '979', '817', '711', '411', '286', '370', '431', '520', '605', '646', '650', '463', '367', '342', '375', '437', '289', '174', '271', '347', '388', '413', '197', 0, '113', '265', '347', '326'], ['669', '829', '867', '930', '934', '908', '746', '640', '340', '399', '483', '544', '633', '718', '759', '762', '575', '479', '454', '487', '549', '401', '287', '384', '460', '501', '526', '310', '113', 0, '152', '256', '235'], ['777', '871', '909', '972', '976', '950', '788', '682', '382', '507', '591', '681', '778', '863', '904', '868', '727', '631', '606', '639', '701', '553', '439', '536', '616', '653', '678', '448', '265', '152', 0, '298', '319'], ['479', '573', '611', '674', '678', '652', '490', '384', '84', '209', '293', '383', '480', '565', '606', '570', '737', '683', '658', '665', '603', '606', '491', '394', '318', '511', '536', '150', '347', '256', '298', 0, '21'], ['488', '594', '632', '695', '699', '673', '511', '405', '105', '218', '302', '381', '470', '555', '596', '560', '727', '662', '637', '644', '582', '585', '470', '373', '297', '490', '515', '129', '326', '235', '319', '21', 0]]
names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Z','X','Y','W','Q','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AR','AS','AT','AU','AV','AZ','AX','AY','AW','AQ']

G = {}
for x in range(0,len(coords)):
        temp = {}
        for y in range(0,len(coords)):
                if(int(distance[x][y])==0):
                        continue
                temp[names[y]] = int(distance[x][y])
        G[names[x]] = temp

#print G
print Dijkstra(G,"C","A")
print "END"

let1 = "B"
let1num = 0
let2 = "C"
let2num = 0

for i in range(0,len(names)):
        if let1 is names[i]:
                let1num = i
        if let2 is names[i]:
                let2num = i
print let1
print let1num
print coords[let1num][0], coords[let1num][1]
print
print let2
print let2num
print coords[let2num][0], coords[let2num][1]
print
print distance[let1num][let2num]
