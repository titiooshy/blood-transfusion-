import networkx as nx

veins = nx.Graph()


for i in range(1, 184):
    veins.add_node(i)


veins.remove_node(51)
veins.add_node(51, {"color": "red"})


# head edges
veins.add_edge_from(
    [
        (44, 46),  # left external jugular vein
        (46, 45),  # space between internal and external left veins
        (43, 45),  # left internal jugular vein
        (42, 37),  # right internal jugular vein
        (41, 36),  # right external jugular vein
        (38, 181),  # inferior thyroid vein
        (39, 181),  # inferior thyroid vein
        (40, 181),  # inferior thyroid vein
        (45, 181),  # space from left internal jugular vein to inferior thyroid vein
        (36, 37),  # space between internal and external right veins
        (25, 36),  # small vein on right side of neck
    ]
)


# chest and ribs edges
veins.add_edges_from(
    [
        (181, 182),
        (37, 182),  # subclavian vein
        (182, 51),  # path to heart
        (182, 47),  # pulmonary arteries
        (48, 182),  # pulmonary arteries
        (49, 182),  # pulmonary arteries
        (182, 50),  # pulmonary arteries
        (169, 182),  # inferior vena cava
        (151, 167),  # intercostal vein
        (152, 166),  # intercostal vein
        (153, 165),  # intercostal vein
        (154, 164),  # intercostal vein
        (155, 163),  # intercostal vein
        (156, 162),  # intercostal vein
        (157, 161),  # intercostal vein
        (158, 160),  # intercostal vein
        (159, 37),  # intercostal vein
        (160, 37),  # internal thoracic vein
        (167, 166),  # internal thoracic vein
        (166, 165),  # internal thoracic vein
        (165, 164),  # internal thoracic vein
        (164, 163),  # internal thoracic vein
        (163, 162),  # internal thoracic vein
        (162, 161),  # internal thoracic vein
        (161, 160),  # internal thoracic vein
        (168, 169),  # hepatic vein
        (170, 169),  # hepatic vein
        (169, 51),  # inferior vena cava
        (150, 34),  # thoracoepigastric
        (35, 36),  # subclavian vein
        (183, 46),  # subclavian vein
    ]
)


# left foot and leg edges
veins.add_edges_from(
    [
        (87, 92),  # deep plantar veins
        (86, 91),  # dorsal digital vein
        (85, 88),  # dorsal digital vein
        (84, 89),  # dorsal digital vein
        (83, 91),  # dorsal digital vein
        (82, 90),  # dorsal digital vein
        (89, 90),  # dorsal venous arch
        (88, 89),  # dorsal venous arch
        (88, 92),  # dorsal venous arch
        (90, 91),  # dorsal venous arch
        (90, 93),  # deep plantar vein
        (91, 94),  # deep plantar vein
        (94, 96),  # top of foot
        (94, 130),  # anterior/posterior tibial vein
        (96, 130),  # anterior/posterior tibial vein
        (130, 132),  # popliteal vein
        (96, 132),  # small saphenous vein
        (131, 132),  # superior genicular vein
        (129, 132),  # superior genicular vein
        (128, 132),  # superior genicular vein
        (127, 132),  # superior genicular vein
        (132, 95),  # femoral vein
        (126, 125),  # accessory saphenous vein
        (92, 125),  # great saphenous vein
        (125, 95),  # great saphenous vein
        (133, 95),  # deep femoral vein
        (134, 95),  # perforating branches
        (135, 95),  # perforating branches
    ]
)


# right foot and leg edges
veins.add_edges_from(
    [
        (101, 100),  # deep planatr veins
        (102, 111),  # dorsal digital vein
        (103, 110),  # dorsal digital vein
        (104, 109),  # dorsal digital vein
        (105, 108),  # dorsal digital vein
        (106, 107),  # dorsal digital vein
        (107, 114),  # dorsal venous arch
        (108, 107),  # dorsal venous arch
        (111, 112),  # dorsal venous arch
        (111, 100),  # dorsal venous arch
        (110, 112),  # dorsal venous arch
        (110, 111),  # dorsal venous arch
        (110, 108),  # dorsal venous arch
        (114, 115),  # anterior/posterior tibial vein
        (114, 122),  # small saphenous
        (112, 114),  # dorsal venous arch
        (115, 116),  # anterior/posterior tibial vein
        (116, 122),  # inferior genicular vein
        (117, 122),  # inferior genicular vein
        (118, 122),  # inferior genicular vein
        (119, 122),  # inferior genicular vein
        (120, 122),  # inferior genicular vein
        (100, 124),  # great saphenous vein
        (121, 124),  # accessory saphenous vein
        (122, 145),  # femoral vein
        (123, 145),  # deep femoral vein
        (124, 145),  # great saphenous vein
        (146, 145),  # perforating branches
        (149, 148),  # perforating branches
        (147, 148),  # perforating branches
        (148, 145),  # perforating branches
    ]
)


# pelivs and lungs edges
veins.add_edges_from(
    [
        (145, 143),  # external iliac vein
        (141, 143),  # internal iliac vein
        (143, 144),  # common iliac vein
        (136, 144),  # common iliac vein
        (142, 136),  # internal iliac vein
        (95, 136),  # external iliac vein
        (137, 171),  # testicularis vein
        (140, 176),  # testicularis vein
        (130, 95),  # external pudendal vein
        (139, 145),  # external pudendal vein
        (150, 145),  # inferior epigastric vein
        (177, 171),  # renal vein
        (178, 171),  # renal vein
        (179, 171),  # renal vein
        (180, 171),  # renal vein
        (171, 176),  # renal vein
        (172, 176),  # renal vein
        (173, 172),  # renal vein
        (174, 172),  # renal vein
        (175, 172),  # renal vein
    ]
)


# left arm and hand edges
veins.add_edges_from(
    [
        (74, 73),  # palmar digital vein
        (75, 72),  # palmar digital vein
        (76, 72),  # palmar digital vein
        (77, 71),  # palmar digital vein
        (78, 71),  # palmar digital vein
        (79, 70),  # palmar digital vein
        (80, 89),  # palmar digital vein
        (81, 67),  # palmar digital vein
        (66, 62),  # palmar digital vein
        (63, 62),  # deep palmar arch
        (63, 64),  # deep palmar arch
        (64, 65),  # deep palmar arch
        (73, 65),  # superficial palmar arch
        (72, 73),  # superficial palmar arch
        (71, 70),  # superficial palmar arch
        (71, 68),  # superficial palmar arch
        (70, 69),  # palmar digital vein
        (69, 67),  # superficial palmar arch
        (67, 63),  # palmar digital vein
        (62, 61),  # ulnar vein
        (63, 61),  # median antebranchial vein
        (69, 68),  # superficial palmar arch
        (68, 64),  # superficial palmar arch
        (64, 60),  # median antebranchial vein
        (65, 59),  # cephalic vein
        (60, 58),  #
        (60, 59),  #
        (61, 58),  #
        (61, 55),  # ulnar vein
        (58, 56),  # median antebranchial vein
        (56, 54),  # median antebranchial vein
        (54, 53),  # median cubital vein
        (54, 55),  # median cubital vein
        (59, 57),  # median antebranchial vein
        (57, 53),  # cephalic vein
        (53, 183),  # axillary vein
        (55, 184),  # cephalic vein
        (52, 184),  # brachial vein
        (184, 183),  # cephalic vein
    ]
)


# right arm and hand edges
veins.add_edges_from(
    [
        (1, 14),  # palmar digital vein
        (2, 13),  # palmar digital vein
        (3, 13),  # palmar digital vein
        (4, 12),  # palmar digital vein
        (5, 113),  # palmar digital vein
        (6, 11),  # palmar digital vein
        (7, 11),  # palmar digital vein
        (8, 10),  # palmar digital vein
        (9, 16),  # palmar digital vein
        (10, 18),  # palmar digital vein
        (14, 19),  # palmar digital vein
        (18, 19),  # superficial palmar arch
        (16, 15),  # median antebranchial vein
        (16, 17),  #
        (16, 15),  # median antebranchial vein
        (19, 15),  # superficial palmar arch
        (18, 113),  # deep palmar arch
        (11, 10),  # superficial palmar arch
        (11, 113),  # palmar digital vein
        (13, 113),  # palmar digital veins
        (12, 11),  # superficial palmar arch
        (12, 13),  # superficial palmar arch
        (13, 14),  # superficial palmar arch
        (18, 16),  # deep palmar arch
        (19, 16),  # deep palmar arch
        (17, 23),  # median antebranchial vein
        (23, 26),  #
        (24, 26),  # cephalic vein
        (26, 27),  # cephalic vein
        (113, 28),  #
        (27, 28),  # median cubital vein
        (27, 35),  # cephalic vein
        (28, 29),  # median cubital vein
        (15, 21),  # median antebranchial vein
        (21, 22),  # median antebranchial vein
        (20, 22),  # cephalic vein
        (22, 29),  # basilic vein
        (29, 31),  # basilic vein
        (30, 31),  # brachial vein
        (31, 33),  # axillary vein
        (32, 33),  # brachial vein
        (33, 34),  # axillary vein
        (34, 35),  # axillary vein
    ]
)
