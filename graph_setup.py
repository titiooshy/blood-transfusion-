import networkx as nx

veins = nx.DiGraph()


for i in range(1, 184):
    veins.add_node(i)


veins.remove_node(51)
veins.add_node(51, color="red")


# head edges
veins.add_weighted_edges_from(
    [
        (44, 46, 8),  # left external jugular vein
        (46, 45, 1),  # space between internal and external left veins
        (43, 45, 10),  # left internal jugular vein
        (42, 37, 10),  # right internal jugular vein
        (41, 36, 8),  # right external jugular vein
        (38, 181, 4),  # inferior thyroid vein
        (39, 181, 4),  # inferior thyroid vein
        (40, 181, 4),  # inferior thyroid vein
        (45, 181, 4),  # space from left internal jugular vein to inferior thyroid vein
        (36, 37, 1),  # space between internal and external right veins
        (25, 36, 1),  # small vein on right side of neck
    ]
)


# chest and ribs edges
veins.add_weighted_edges_from(
    [
        (181, 182, 2),
        (37, 182, 2),  # subclavian vein
        (182, 51, 5),  # path to heart
        (182, 47, 5),  # pulmonary arteries
        (48, 182, 5),  # pulmonary arteries
        (49, 182, 5),  # pulmonary arteries
        (182, 50, 5),  # pulmonary arteries
        (169, 182, 7),  # inferior vena cava
        (151, 167, 3),  # intercostal vein
        (152, 166, 3),  # intercostal vein
        (153, 165, 3),  # intercostal vein
        (154, 164, 3),  # intercostal vein
        (155, 163, 3),  # intercostal vein
        (156, 162, 3),  # intercostal vein
        (157, 161, 2),  # intercostal vein
        (158, 160, 2),  # intercostal vein
        (159, 37, 2),  # intercostal vein
        (160, 37, 1),  # internal thoracic vein
        (167, 166, 1),  # internal thoracic vein
        (166, 165, 1),  # internal thoracic vein
        (165, 164, 1),  # internal thoracic vein
        (164, 163, 1),  # internal thoracic vein
        (163, 162, 1),  # internal thoracic vein
        (162, 161, 1),  # internal thoracic vein
        (161, 160, 1),  # internal thoracic vein
        (168, 169, 11),  # hepatic vein
        (170, 169, 11),  # hepatic vein
        (150, 34, 8),  # thoracoepigastric vein
        (35, 36, 6),  # subclavian vein
        (183, 46, 6),  # subclavian vein
    ]
)


# left foot and leg edges
veins.add_weighted_edges_from(
    [
        (87, 92, 5),  # deep plantar veins
        (86, 91, 3),  # dorsal digital vein
        (85, 88, 1),  # dorsal digital vein
        (84, 89, 1),  # dorsal digital vein
        (83, 91, 3),  # dorsal digital vein
        (82, 90, 2),  # dorsal digital vein
        (89, 90, 1),  # dorsal venous arch
        (88, 89, 1),  # dorsal venous arch
        (88, 92, 5),  # dorsal venous arch
        (90, 91, 2),  # dorsal venous arch
        (90, 93, 4),  # deep plantar vein
        (91, 94, 5),  # deep plantar vein
        (94, 96, 2),  # top of foot
        (94, 130, 11),  # anterior/posterior tibial vein
        (96, 130, 10),  # anterior/posterior tibial vein
        (130, 132, 3),  # popliteal vein
        (96, 132, 14),  # small saphenous vein
        (131, 132, 3),  # superior genicular vein
        (129, 132, 3),  # superior genicular vein
        (128, 132, 3),  # superior genicular vein
        (127, 132, 3),  # superior genicular vein
        (132, 95, 14),  # femoral vein
        (126, 125, 3.5),  # accessory saphenous vein
        (92, 125, 29),  # great saphenous vein
        (125, 95, 5),  # great saphenous vein
        (133, 95, 4),  # deep femoral vein
        (134, 95, 1),  # perforating branches
        (135, 95, 2),  # perforating branches
    ]
)


# right foot and leg edges
veins.add_weighted_edges_from(
    [
        (101, 100, 5),  # deep planatr veins
        (102, 111, 1.5),  # dorsal digital vein
        (103, 110, 1.5),  # dorsal digital vein
        (104, 109, 1.5),  # dorsal digital vein
        (105, 108, 1.5),  # dorsal digital vein
        (106, 107, 2),  # dorsal digital vein
        (107, 114, 1),  # dorsal venous arch
        (108, 107, 1),  # dorsal venous arch
        (111, 112, 1),  # dorsal venous arch
        (111, 100, 1),  # dorsal venous arch
        (110, 112, 1),  # dorsal venous arch
        (110, 111, 1),  # dorsal venous arch
        (110, 108, 1),  # dorsal venous arch
        (114, 115, 3),  # anterior/posterior tibial vein
        (114, 122, 14),  # small saphenous
        (112, 114, 2),  # dorsal venous arch
        (115, 116, 11),  # anterior/posterior tibial vein
        (116, 122, 3),  # popliteal vein
        (117, 122, 3),  # inferior genicular vein
        (118, 122, 3),  # inferior genicular vein
        (119, 122, 3),  # inferior genicular vein
        (120, 122, 3),  # inferior genicular vein
        (100, 124, 29),  # great saphenous vein
        (121, 124, 3.5),  # accessory saphenous vein
        (122, 145, 14),  # femoral vein
        (123, 145, 4),  # deep femoral vein
        (124, 145, 5),  # great saphenous vein
        (146, 145, 2.5),  # perforating branches
        (149, 148, 1),  # perforating branches
        (147, 148, 1),  # perforating branches
        (148, 145, 2.5),  # perforating branches
    ]
)


# pelivs and lungs edges
veins.add_weighted_edges_from(
    [
        (145, 143, 1),  # external iliac vein
        (141, 143, 3),  # internal iliac vein
        (143, 144, 5.5),  # common iliac vein
        (136, 144, 5.5),  # common iliac vein
        (142, 136, 3),  # internal iliac vein
        (95, 136, 1),  # external iliac vein
        (137, 171, 4.5),  # testicularis vein
        (140, 176, 4.5),  # testicularis vein
        (130, 95, 2),  # external pudendal vein
        (139, 145, 2),  # external pudendal vein
        (150, 145, 12),  # inferior epigastric vein
        (177, 171, 6),  # renal vein
        (178, 171, 6),  # renal vein
        (179, 171, 6),  # renal vein
        (180, 171, 6),  # renal vein
        (171, 176, 1),  # renal vein
        (172, 176, 1),  # renal vein
        (173, 172, 3),  # renal vein
        (174, 172, 3),  # renal vein
        (175, 172, 3),  # renal vein
    ]
)


# left arm and hand edges
veins.add_weighted_edges_from(
    [
        (74, 73, 3),  # palmar digital vein
        (75, 72, 3),  # palmar digital vein
        (76, 72, 3),  # palmar digital vein
        (77, 71, 3),  # palmar digital vein
        (78, 71, 3),  # palmar digital vein
        (79, 70, 3),  # palmar digital vein
        (80, 89, 3),  # palmar digital vein
        (81, 67, 3),  # palmar digital vein
        (66, 62, 3),  # palmar digital vein
        (63, 62, 1),  # deep palmar arch
        (63, 64, 1),  # deep palmar arch
        (64, 65, 1),  # deep palmar arch
        (73, 65, 3),  # superficial palmar arch
        (72, 73, 1.5),  # superficial palmar arch
        (71, 70, 1),  # superficial palmar arch
        (71, 68, 1.5),  # superficial palmar arch
        (70, 69, 1),  # palmar digital vein
        (69, 67, 1),  # superficial palmar arch
        (67, 63, 1.5),  # palmar digital vein
        (62, 61, 1.5),  # ulnar vein
        (63, 61, 2),  # median antebranchial vein
        (69, 68, 1),  # superficial palmar arch
        (68, 64, 1.5),  # superficial palmar arch
        (64, 60, 2),  # median antebranchial vein
        (65, 59, 3),  # cephalic vein
        (60, 58, 1),  #
        (60, 59, 1),  #
        (61, 58, 1),  #
        (61, 55, 4.5),  # ulnar vein
        (58, 56, 2.5),  # median antebranchial vein
        (56, 54, 1.5),  # median antebranchial vein
        (54, 53, 1),  # median cubital vein
        (54, 55, 1),  # median cubital vein
        (59, 57, 2),  # median antebranchial vein
        (57, 53, 2),  # cephalic vein
        (53, 183, 11),  # axillary vein
        (55, 184, 10),  # cephalic vein
        (52, 184, 1.5),  # brachial vein
        (184, 183, 1),  # cephalic vein
    ]
)


# right arm and hand edges
veins.add_weighted_edges_from(
    [
        (1, 14, 3),  # palmar digital vein
        (2, 13, 3),  # palmar digital vein
        (3, 13, 3),  # palmar digital vein
        (4, 12, 3),  # palmar digital vein
        (5, 113, 6),  # palmar digital vein
        (6, 11, 3),  # palmar digital vein
        (7, 11, 3),  # palmar digital vein
        (8, 10, 3),  # palmar digital vein
        (9, 16, 6),  # palmar digital vein
        (10, 18, 2),  # palmar digital vein
        (14, 19, 3),  # palmar digital vein
        (18, 19, 2.5),  # superficial palmar arch
        (16, 15, 5),  # median antebranchial vein
        (16, 17, 1),  #
        (16, 15, 2),  # median antebranchial vein
        (19, 15, 2),  # superficial palmar arch
        (18, 113, 1),  # deep palmar arch
        (11, 10, 1),  # superficial palmar arch
        (11, 113, 3),  # palmar digital vein
        (13, 113, 3),  # palmar digital veins
        (12, 11, 1),  # superficial palmar arch
        (12, 13, 1),  # superficial palmar arch
        (13, 14, 1),  # superficial palmar arch
        (18, 16, 1),  # deep palmar arch
        (19, 16, 1),  # deep palmar arch
        (17, 23, 6),  # median antebranchial vein
        (23, 26, 2),  #
        (24, 26, 4.5),  # cephalic vein
        (26, 27, 4.5),  # cephalic vein
        (113, 28, 10),  #
        (27, 28, 2.5),  # median cubital vein
        (27, 35, 9),  # cephalic vein
        (28, 29, 2.5),  # median cubital vein
        (15, 21, 5),  # median antebranchial vein
        (21, 22, 2),  # median antebranchial vein
        (20, 22, 4.5),  # cephalic vein
        (22, 29, 3.5),  # basilic vein
        (29, 31, 3.5),  # basilic vein
        (30, 31, 1),  # brachial vein
        (31, 33, 2),  # axillary vein
        (32, 33, 1),  # brachial vein
        (33, 34, 2),  # axillary vein
        (34, 35, 2),  # axillary vein
    ]
)
