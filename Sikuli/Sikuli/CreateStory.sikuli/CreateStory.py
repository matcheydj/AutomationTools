title=["Ensure rsyslog or syslog-ng is installed"]
#for i in range(3):
for i in range(len(title)):
#  rightClick("1441009492166.png")

#  click("1440049508703.png")
#  type(Key.DELETE)

#  type("Development")
#  rightClick("1452223443328.png")doubleClick()
# if exists("1489564160154.png"):
#   click("1489563639853.png")
#   click("1489563238367.png")
#   type(Key.DELETE)

#   type("Closed")
#   click("1489563878243.png")
# click("1491977204966.png")
# click("1493196396544.png")
 click("1493198059680.png")
 onAppear("1493198237558.png",click("1493198258992.png"))
 wait(2)
 type("Create content for "+title[i])
 click("1491977294992.png")
 click("1491977430263.png")
 wait(4)


 click(find("1493199484109.png").below(58))
 wait(2)
 onAppear("1493198237558.png",click("1493198258992.png"))
 wait(2)
 type("Test content for "+title[i])
 click("1491977294992.png")
 click("1491977430263.png")
 wait(4)
 
 wait(3)
 
# if exists("1490866678153.png"):
#   click("1490866764356.png")
#   click("1490866951793.png")
#   type(Key.DELETE)
#   type("Done")