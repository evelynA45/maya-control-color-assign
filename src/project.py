

# Take left controls and color them
def left_color():
    for con in cmds.ls('L_*_CON'):
        shapes = cmds.listRelatives(con, s=True)
        cmds.setAttr(shapes[0] + '.overrideEnabled', 1)
#Take right controls and color them

#Take middle controls and color them