import sys
import time

# Take left controls and color them

def left_color():
    for con in cmds.ls('L_*_CON'):
        shapes = cmds.listRelatives(con, s=True)
        cmds.setAttr(shapes[0] + '.overrideEnabled', 1)
        cmds.setAttr(shapes[0] + '.overrideColor', 6)

#Take right controls and color them

def right_color():
    for con in cmds.ls('R_*_CON'):
        shapes = cmds.listRelatives(con, s=True)
        cmds.setAttr(shapes[0] + '.overrideEnabled', 1)
        cmds.setAttr(shapes[0] + '.overrideColor', 13)

#Take middle controls and color them

def middle_color():
    for con in cmds.ls('*_CON'):
        if con.startswith('L') or con.startswith('R'):
            continue
        shapes = cmds.listRelatives(con, s=True)
        cmds.setAttr(shapes[0] + '.overrideEnabled', 1)
        cmds.setAttr(shapes[0] + '.overrideColor', 17)
        
#Print effect
 
def typewriter_print(text, delay=0.05):
     for char in text:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(delay)
     print()
        
#Run in main function

def main():
    typewriter_print("Coloring controls...")
    left_color()
    right_color()
    middle_color()
    typewriter_print("Coloring done!", delay=0.05)

if __name__ == "__main__":
    main()