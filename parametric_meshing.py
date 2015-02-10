import rhinoscriptsyntax as rs
import random

def drawObjects():
    #get mesh to be used
    objs = rs.GetObjects("Select mesh object", rs.filter.mesh, True)
    if not objs: return

    #offset mesh for better fitting
    #offset = rs.GetInteger("offset mesh by",3,3,8)
    #rs.MeshOffset( objs, offset)

    vertices = rs.MeshVertices(objs)
    if vertices:
        pointcloud=rs.AddPointCloud(vertices)
    rad = random.randint(0,1)
    points = rs.PointCloudPoints(pointcloud)
    if points:
        for point in points:
            #print point
            #for xn in range (0, points.length)
            x= point[0]+random.randint(0,1)
            y=point[1]
            z=point[2]+random.randint(0,1)
            rad = rad*(.75)
            pt = (x,y,z)
            sphere = rs.AddSphere(pt, rad)

    

rs.EnableRedraw(False)

drawObjects()
            
rs.Redraw()