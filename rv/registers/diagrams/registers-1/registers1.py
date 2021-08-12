# This class represents a box with coordinates (x, y), size (width, height), text (text) and color (c). 
class Box(object):
  def __init__(self, x, y, width, height, txt, c):
    strokeWeight(2);
    stroke(0)
    fill(c)
    rectMode(CORNERS)
    rect(x, y, x + width, y + height);
    fill(0)
    textAlign(CENTER, TOP);
    textSize(10);
    text(txt, x + width / 2, y + 10);

class XorBox(object):
  def __init__(self, x, y, width, height, c):
    strokeWeight(2);
    stroke(0)
    fill(c)
    rectMode(CORNERS)
    rect(x, y, x + width, y + height);
    fill(255)
    circle(x + width / 2, y + 15, 20)
    line(x + (width / 2) - 4, y + 15, x + (width / 2) + 4, y + 15)
    line(x + width / 2, y + 11, x + width / 2, y + 19)
    
class MuxBox(object):
  def __init__(self, x, y, width, height, c):
    strokeWeight(2);
    stroke(0)
    fill(c)
    rectMode(CORNERS)
    beginShape()
    vertex(x, y)
    vertex(x + width, y + 5)
    vertex(x + width, y + height - 5);
    vertex(x, y + height)
    endShape(CLOSE)
    
class Arrow(object):
  def __init__(self, x1, y1, x2, y2, width, txt, c):
    stroke(c)
    strokeWeight(width);
    fill(c)
    if y1 == y2 and x1 <= x2: #horizontal line from left to right
      line(x1, y1, x2 - 10, y2)
      noStroke()
      triangle(x2 - 10, y1 - 3, x2, y1, x2 - 10, y1 + 3)
      textAlign(RIGHT, BOTTOM)
      textSize(10)
      fill(0)
      text(txt, x2 - 10, y1 + 2)
    elif y1 == y2 and x1 > x2: #horizontal line from right to left
      line(x1, y1, x2 + 10, y2)
      noStroke()
      triangle(x2 + 10, y1 - 3, x2, y1, x2 + 10, y1 + 3)
    elif x1 == x2 and y1 <= y2: #vertical line from top to bottom
      line(x1, y1, x2, y2 - 10)
      noStroke()
      triangle(x1 - 3, y2 - 10, x1, y2, x1 + 3, y2 - 10)
      textAlign(RIGHT, BOTTOM)
      textSize(10)
      fill(0)
    elif x1 == x2 and y1 > y2: #vertical line from bottom to top
      line(x1, y1, x2, y2 + 10)
      noStroke()
      triangle(x1 - 3, y2 + 10, x1, y2, x1 + 3, y2 + 10)
      textAlign(RIGHT, BOTTOM)
      textSize(10)
      fill(0)
      rotate(-PI/2.0)
      text(txt, - y1 + 5 * len(txt), x2)
      rotate(PI/2.0)
    fill(0)

class TextCircle(object):
  def __init__(self, x, y, txt, c):
    strokeWeight(2)
    stroke(0)
    fill(c)
    circle(x, y, 25)
    fill(0)
    textSize(10)
    text(txt, x, y + 5)

class LineDot(object):
  def __init__(self, x, y, c):
    strokeWeight(2)
    stroke(0)
    fill(c)
    noStroke()
    circle(x, y, 6)

class ClkInput(object):
  def __init__(self, x, y):
    strokeWeight(1)
    stroke(0)
    line(x, y, x + 5, y + 5)
    line(x + 5, y + 5, x, y + 10)
    noStroke()

#-----------------------------------------------------------------
# Node
class NodeType(object):
  def __init__(self):
    self.blue_color = color(160, 160, 240)
    self.red_color = color(240, 160, 160)
    self.green_color = color(160, 240, 160)
    self.cols = ["A", "B", "C", "D", "E", "F", "G", "H"]

#-----------------------------------------------------------------
# Type A Node
class NodeTypeA(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    a1_txt = "op1_addr{0}".format(col)
    a2_txt = "op2_addr{0}".format(col)
    wb_a_txt = "wb_addr{0}".format(col)
    wb_a2_txt = "wb_addr{0}".format(row)
    Arrow(x, y + 10, x + 100, y + 10, 1, "a1", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(a1_txt, x, y + 12)
    Arrow(x, y + 20, x + 100, y + 20, 1, "a2", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(wb_a_txt, x, y + 22)
    Arrow(x, y + 30, x + 100, y + 30, 1, "a3", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(a2_txt, x, y + 32)      
    Arrow(x + 20, y + 40, x + 100, y + 40, 1, "a4", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(wb_a2_txt, x + 20, y + 42)  
    Arrow(x + 10, y + 50, x + 100, y + 50, 2, "w_data", self.green_color)
    Arrow(x + 30, y + 70, x + 100, y + 70, 1, "we", self.blue_color)
    Arrow(x + 50, y + 90, x + 100, y + 90, 1, "clk", self.blue_color)
    Arrow(x + 50, y + 100, x + 100, y + 100, 1, "clk_n", self.blue_color)
    strokeWeight(1)
    stroke(self.red_color)
    line(x + 20, y + 40, x + 20, y + 230)
    strokeWeight(2)
    stroke(self.green_color)
    line(x + 10, y + 50, x + 10, y + 240)
    strokeWeight(1)
    stroke(self.blue_color)
    line(x + 30, y + 70, x + 30, y + 220)
    
#-----------------------------------------------------------------
# Type B Node
class NodeTypeB(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    a1_txt = "op1_addr{0}".format(col)
    wb_a2_txt = "wb_addr{0}".format(row)
    Arrow(x, y + 10, x + 100, y + 10, 2, "a1", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(a1_txt, x, y + 12)
    Arrow(x, y + 30, x + 100, y + 30, 2, "a3", self.red_color)
    Arrow(x + 20, y + 40, x + 100, y + 40, 2, "a4", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(wb_a2_txt, x + 20, y + 42)  
    Arrow(x + 10, y + 50, x + 100, y + 50, 2, "w_data", self.green_color)
    Arrow(x + 30, y + 70, x + 100, y + 70, 1, "we", self.blue_color)
    Arrow(x + 50, y + 90, x + 100, y + 90, 1, "clk", self.blue_color)
    Arrow(x + 50, y + 100, x + 100, y + 100, 1, "clk_n", self.blue_color)

class XorOutput(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    txt = """3-port
cell"""
    xor_in1_txt = "{0}{1}_1".format(self.cols[col], (0, 1)[row <= 0])
    xor_in2_txt = "{0}{1}_1".format(self.cols[col], (1, 2)[row <= 1])
    xor_in3_txt = "{0}{1}_1".format(self.cols[col], (2, 3)[row <= 2])
    xor_in4_txt = "{0}{1}_1".format(self.cols[col], (3, 4)[row <= 3])
    xor_in5_txt = "{0}{1}_1".format(self.cols[col], (4, 5)[row <= 4])
    xor_in6_txt = "{0}{1}_1".format(self.cols[col], (5, 6)[row <= 5])
    xor_in7_txt = "{0}{1}_1".format(self.cols[col], (6, 7)[row <= 6])
    xor_in8_txt = "{0}{1}_2".format(self.cols[col], (0, 1)[row <= 0])
    xor_in9_txt = "{0}{1}_2".format(self.cols[col], (1, 2)[row <= 1])
    xor_in10_txt = "{0}{1}_2".format(self.cols[col], (2, 3)[row <= 2])
    xor_in11_txt = "{0}{1}_2".format(self.cols[col], (3, 4)[row <= 3])
    xor_in12_txt = "{0}{1}_2".format(self.cols[col], (4, 5)[row <= 4])
    xor_in13_txt = "{0}{1}_2".format(self.cols[col], (5, 6)[row <= 5])
    xor_in14_txt = "{0}{1}_2".format(self.cols[col], (6, 7)[row <= 6])
    op1_txt = "op1_data{0}".format(row)
    op2_txt = "op2_data{0}".format(row)
    Arrow(x + 150, y + 10, x + 245, y + 10, 2, "", self.green_color)
    Arrow(x + 120, y + 120, x + 190, y + 120, 2, "", self.green_color)
    Arrow(x + 155, y + 30, x + 190, y + 30, 2, xor_in1_txt, self.green_color)
    Arrow(x + 155, y + 40, x + 190, y + 40, 2, xor_in2_txt, self.green_color)
    Arrow(x + 155, y + 50, x + 190, y + 50, 2, xor_in3_txt, self.green_color)
    Arrow(x + 155, y + 60, x + 190, y + 60, 2, xor_in4_txt, self.green_color)
    Arrow(x + 155, y + 70, x + 190, y + 70, 2, xor_in5_txt, self.green_color)
    Arrow(x + 155, y + 80, x + 190, y + 80, 2, xor_in6_txt, self.green_color)
    Arrow(x + 155, y + 90, x + 190, y + 90, 2, xor_in7_txt, self.green_color)
    Arrow(x + 155, y + 130, x + 190, y + 130, 2, xor_in8_txt, self.green_color)
    Arrow(x + 155, y + 140, x + 190, y + 140, 2, xor_in9_txt, self.green_color)
    Arrow(x + 155, y + 150, x + 190, y + 150, 2, xor_in10_txt, self.green_color)
    Arrow(x + 155, y + 160, x + 190, y + 160, 2, xor_in11_txt, self.green_color)
    Arrow(x + 155, y + 170, x + 190, y + 170, 2, xor_in12_txt, self.green_color)
    Arrow(x + 155, y + 180, x + 190, y + 180, 2, xor_in13_txt, self.green_color)
    Arrow(x + 155, y + 190, x + 190, y + 190, 2, xor_in14_txt, self.green_color)
    Arrow(x + 275, y + 10, x + 340, y + 10, 2, op1_txt, self.green_color)
    Arrow(x + 220, y + 120, x + 340, y + 120, 2, op2_txt, self.green_color)
    Arrow(x + 220, y + 30, x + 245, y + 30, 2, "", self.green_color)
    XorBox(x + 245, y, 30, 40, self.green_color)
    XorBox(x + 190, y + 20, 30, 80, self.green_color)
    XorBox(x + 190, y + 110, 30, 90, self.green_color)
    strokeWeight(2)
    stroke(self.green_color)
    line(x + 230, y + 30, x + 230, y + 210)
    Box(x + 100, y, 50, 130, txt, self.blue_color)
#-----------------------------------------------------------------
# Type C Node
class NodeTypeC(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    box1_txt = """(addr!=0
&rst_n
&clk)|
!rst_n"""
    a1_txt = "op1_addr{0}".format(col)
    a2_txt = "op2_addr{0}".format(col)
    self.wb_a_txt = "wb_addr{0}".format(col)
    self.wb_a2_txt = "wb_addr{0}".format(row)
    w_data_txt = "w_data{0}".format(row)
    Arrow(x - 270, y + 10, x + 100, y + 10, 2, "a1", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(a1_txt, x - 270, y + 12)
    Arrow(x - 270, y + 30, x + 100, y + 30, 2, "a3", self.red_color)
    textAlign(LEFT, BOTTOM)
    text(a2_txt, x - 270, y + 32)      
    Arrow(x - 70, y + 40, x + 100, y + 40, 2, "a4", self.red_color)
    Arrow(x - 80, y + 50, x + 100, y + 50, 2, "w_data", self.green_color)
    Arrow(x + 30, y + 70, x + 100, y + 70, 1, "we", self.blue_color)
    Arrow(x + 50, y + 90, x + 100, y + 90, 1, "clk", self.blue_color)
    Arrow(x + 50, y + 100, x + 100, y + 100, 1, "clk_n", self.blue_color)
    strokeWeight(2)
    stroke(self.red_color)
    line(x - 70, y + 40, x - 70, y + 230)
    LineDot(x - 70, y + 80, self.red_color)
    strokeWeight(2)
    stroke(self.green_color)
    line(x - 80, y + 50, x - 80, y + 240)
    LineDot(x - 80, y + 130, self.green_color)
    strokeWeight(1)
    stroke(self.blue_color)
    line(x + 40, y + 70, x + 40, y + 220)
    LineDot(x + 40, y + 70, self.blue_color)
    Box(x - 20, y + 60, 50, 80, box1_txt, self.blue_color)
    Arrow(x - 70, y + 70, x - 20, y + 70, 2, "", self.red_color)
    Arrow(x - 60, y + 80, x - 20, y + 80, 1, "rst_n", self.blue_color)
    Arrow(x - 60, y + 90, x - 20, y + 90, 1, "clk_n", self.blue_color)
    strokeWeight(2)
    stroke(self.red_color)
    line(x - 100, y + 80, x - 70, y + 80)
    MuxBox(x - 140, y + 60, 40, 40, self.red_color)
    fill(0)
    textAlign(LEFT, BOTTOM)
    text("sel=1", x - 135, y + 77)
    textAlign(LEFT, BOTTOM)
    text("sel=0", x - 135, y + 95)
    strokeWeight(2)
    stroke(self.green_color)
    line(x - 100, y + 130, x - 80, y + 130)
    MuxBox(x - 140, y + 110, 40, 40, self.green_color)
    fill(0)
    textAlign(LEFT, BOTTOM)
    text("sel=1", x - 135, y + 127)
    textAlign(LEFT, BOTTOM)
    text("sel=0", x - 135, y + 145)
    LineDot(x - 70, y + 70, self.red_color)
    Arrow(x - 160, y + 70, x - 140, y + 70, 2, "", self.red_color)
    Arrow(x - 160, y + 120, x - 140, y + 120, 2, "", self.green_color)
    Arrow(x - 270, y + 90, x - 140, y + 90, 2, "", self.red_color)
    fill(0)
    textAlign(LEFT, BOTTOM)
    text(self.wb_a2_txt, x - 270, y + 90)
    Arrow(x - 190, y + 140, x - 140, y + 140, 2, "", self.green_color)
    TextCircle(x - 170, y + 70, "0", self.red_color)
    TextCircle(x - 170, y + 120, "0", self.green_color)
    XorBox(x - 220, y + 130, 30, 30, self.green_color)
    Arrow(x - 270, y + 140, x - 220, y + 140, 2, w_data_txt, self.green_color)
    Arrow(x - 240, y + 150, x - 220, y + 150, 2, "", self.green_color)
    Arrow(x - 120, y + 110, x - 120, y + 98, 1, "", self.blue_color)
    Arrow(x - 120, y + 200, x - 120, y + 148, 1, "rst_n", self.blue_color)
    strokeWeight(2)
    stroke(self.green_color)
    line(x - 240, y + 150, x - 240, y + 210)

#-----------------------------------------------------------------
# Type DefaultOutput Node
class DefaultOutput(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    out1_txt = "{0}{1}_1".format(self.cols[col], row)
    out2_txt = "{0}{1}_2".format(self.cols[col], row)
    txt = """4-port
cell"""
    Arrow(x + 150, y + 10, x + 190, y + 10, 2, out1_txt, self.green_color)
    Arrow(x + 150, y + 30, x + 190, y + 30, 2, out2_txt, self.green_color)
    Box(x + 100, y, 50, 110, txt, self.blue_color)
#-----------------------------------------------------------------
class Connections(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    strokeWeight(2)
    stroke(self.green_color)
    line(x - 240, y + 210, x + row * 220 + 230, y + 210)
    strokeWeight(1)
    stroke(self.blue_color)
    line(x + 40, y + 220, x + 1720, y + 220)
    strokeWeight(1)
    stroke(self.red_color)
    line(x - 70, y + 230, x + 1710, y + 230)
    strokeWeight(1)
    stroke(self.green_color)
    line(x - 80, y + 240, x + 1700, y + 240)
#-----------------------------------------------------------------
class Connections2(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)
    strokeWeight(2)
    stroke(self.green_color)
    line(x - 240, y + 210, x + row * 220 + 230, y + 210)
    strokeWeight(1)
    stroke(self.blue_color)
    line(x + 40, y + 220, x + 1570, y + 220)
    strokeWeight(1)
    stroke(self.red_color)
    line(x - 70, y + 230, x + 1560, y + 230)
    strokeWeight(1)
    stroke(self.green_color)
    line(x - 80, y + 240, x + 1550, y + 240)
#-----------------------------------------------------------------
class ConnectionDots(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self)    
    LineDot(x + 20, y + 230, self.red_color)
    LineDot(x + 10, y + 240, self.green_color)
    LineDot(x + 30, y + 220, self.blue_color)
#-----------------------------------------------------------------
class XorConnection(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self) 
    strokeWeight(1)
    stroke(self.red_color)
    line(x + 20, y + 40, x + 20, y + 230)
    strokeWeight(2)
    stroke(self.green_color)
    line(x + 10, y + 50, x + 10, y + 240)
    strokeWeight(1)
    stroke(self.blue_color)
    line(x + 30, y + 70, x + 30, y + 220)
#-----------------------------------------------------------------
class XorConnectionDots(NodeType):
  def __init__(self, x, y, col, row):
    NodeType.__init__(self) 
    LineDot(x + 20, y + 230, self.red_color)
    LineDot(x + 10, y + 240, self.green_color)
    LineDot(x + 30, y + 220, self.blue_color)
#-----------------------------------------------------------------
class OutputObjects(NodeType):
  def __init__(self, x, y, rows):
    NodeType.__init__(self)
    for i in range(0, rows):
      Arrow(x - 100, y + i * 90 + 10, x, y + i * 90 + 10, 2, "", self.green_color)
      fill(0)
      textAlign(LEFT, BOTTOM)
      text("op1_data{0}".format(i), x - 100, y + i * 90 + 10)
      Arrow(x - 30, y + i * 90 + 20, x, y + i * 90 + 20, 1, "", self.blue_color)
      Arrow(x + 50, y + i * 90 + 10, x + 150, y + i * 90 + 10, 2, "op1_data{0}_reg".format(i), self.green_color)
      Box(x, y + i * 90, 50, 30, "reg", self.green_color)
      ClkInput(x, y + i * 90 + 15)
      if i > 0:
        LineDot(x - 30, y + i * 90 + 20, self.blue_color)
      #----------------
      Arrow(x - 100, y + i * 90 + 50, x, y + i * 90 + 50, 2, "", self.green_color)
      fill(0)
      textAlign(LEFT, BOTTOM)
      text("op2_data{0}".format(i), x - 100, y + i * 90 + 50)
      Arrow(x - 30, y + i * 90 + 60, x, y + i * 90 + 60, 1, "", self.blue_color)
      Arrow(x + 50, y + i * 90 + 50, x + 150, y + i * 90 + 50, 2, "op2_data{0}_reg".format(i), self.green_color)
      Box(x, y + 40 + i * 90, 50, 30, "reg", self.green_color)
      ClkInput(x, y + i * 90 + 55)
      LineDot(x - 30, y + i * 90 + 60, self.blue_color)
      #----------------
      strokeWeight(1)
      stroke(self.blue_color)
      line(x - 30, y + 20, x - 30, y + 740)
      txt = "clk"
      textAlign(RIGHT, BOTTOM)
      textSize(10)
      fill(0)
      rotate(-PI/2.0)
      text(txt, -y - 740 + 5 * len(txt), x - 30)
      rotate(PI/2.0)
#-----------------------------------------------------------------
class ClkRstNObjects(NodeType):
  def __init__(self, x, y):
    NodeType.__init__(self)
    Arrow(x, y, x + 100, y, 1, "rst_n", self.blue_color)
    Arrow(x, y + 30, x + 40, y + 30, 1, "clk", self.blue_color)
    Arrow(x + 60, y + 30, x + 100, y + 30, 1, "clk_n", self.blue_color)
    strokeWeight(2)
    stroke(0)
    fill(self.blue_color)
    triangle(x + 40, y + 10, x + 40, y + 50, x + 60, y + 30)
    strokeWeight(1)
    fill(255)
    circle(x + 60, y + 30, 6)
#-----------------------------------------------------------------
class LegendObjects(NodeType):
  def __init__(self, x, y):
    NodeType.__init__(self)
    Box(x, y, 150, 120, "Legend", 255)
    Arrow(x + 10, y + 50, x + 140, y + 50, 1, "1-bit control line", self.blue_color)
    Arrow(x + 10, y + 80, x + 140, y + 80, 2, "5-bit control line", self.red_color)
    Arrow(x + 10, y + 110, x + 140, y + 110, 2, "32/64-bit control line", self.green_color)    
#-----------------------------------------------------------------
# Main sheet
def setup():
  size(2700, 2400)
 
def draw():
  #scale(0.5)
  translate(0.0, 0.0);
  array_width = 100
  array_height = 100
  box_width = 60
  box_height = 80
  cols = 8
  rows = cols
  background(255)
  for i in range(0, cols):
    for j in range(0, rows):
      if i == j:
        XorOutput(400 + i * 220, 100 + j * 270, i, j)
      elif i < j:
        DefaultOutput(400 + i * 220, 100 + j * 270, i, j)
      else:
        DefaultOutput(550 + i * 220, 100 + j * 270, i, j)
      #------------------------------------------------------------
      if i == 0:
        NodeTypeC(400, 100 + j * 270, i, j)
        if j < rows - 1:
          Connections(400, 100 + j * 270, i, j)
        else:
          Connections2(400, 100 + j * 270, i, j)
      elif i == j: 
        NodeTypeB(400 + i * 220, 100 + j * 270, i, j)
      elif i < j:
        NodeTypeA(400 + i * 220, 100 + j * 270, i, j)
      else:
        NodeTypeA(550 + i * 220, 100 + j * 270, i, j)
      #-----------------------------------------------------------
      if i > 0 and i < cols - 1:
        if i < j:
          ConnectionDots(400 + i * 220, 100 + j * 270, i, j)
        elif i > j:
          ConnectionDots(550 + i * 220, 100 + j * 270, i, j)
        elif i > 0: # i == j
          XorConnectionDots(400 + i * 220, 100 + j * 270, i, j)
      if i > 0 and i == j:    
          XorConnection(400 + i * 220, 100 + j * 270, i, j)
  OutputObjects(2500, 100, rows)
  ClkRstNObjects(100, 2300)
  LegendObjects(300, 2270)
  #save("~/Pictures/diagram1.jpg")
