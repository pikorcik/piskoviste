import ogr
from .exception import RadiationError

class RadiationGeneralizer:
    def __init__(self):
        pass

    def perform2(self, geometry, geom_id):

        # while True:
        if geometry.GetGeometryCount() > 1:
            count = 0
            for p in geometry:
                # print "pocet pred gener: {}, id: {}".format(p.GetPointCount(), geom_id)
                count = count+p.GetPointCount()
            print "pocet pred gener_celk: {}, id: {}".format(count, geom_id)
        else:
            count = geometry.GetPointCount()
            print "pocet pred gener: {}, id: {}".format(count, geom_id)

        geom_simplified = geometry.Simplify(0.0001)

        if geom_simplified.GetGeometryCount() > 1:
            count = 0
            for p in geom_simplified:
                # print "pocet po gener: {}, id: {}".format(p.GetPointCount(), geom_id)
                count = count + p.GetPointCount()
            print "pocet po gener: {}, id: {}".format(count, geom_id)
        else:
            count = geom_simplified.GetPointCount()
            print "pocet po gener: {}, id: {}".format(count, geom_id)

        if count < 50:
            if geometry.GetGeometryCount() > 1:
                count = 0
                for p in geometry:
                    # print "pocet pred gener: {}, id: {}".format(p.GetPointCount(), geom_id)
                    count = count + p.GetPointCount()
                print "pocet pred gener_celk: {}, id: {}".format(count, geom_id)
            else:
                count = geometry.GetPointCount()
                print "pocet pred gener: {}, id: {}".format(count, geom_id)

            geom_simplified = geometry.Simplify(0.0005)

            if geom_simplified.GetGeometryCount() > 1:
                count = 0
                for p in geom_simplified:
                    # print "pocet po gener: {}, id: {}".format(p.GetPointCount(), geom_id)
                    count = count + p.GetPointCount()
                print "pocet po gener: {}, id: {}".format(count, geom_id)
            else:
                count = geom_simplified.GetPointCount()
                print "pocet po gener: {}, id: {}".format(count, geom_id)

        print "==============="

        return geom_simplified


    def perform(self, geometry, geom_id):
        tolerance = 0.000001

        # print type(geometry)
        ring2 = geometry.GetGeometryRef(0)
        # print "ring2: {}, id: {}".format(ring2.GetPointCount(), geom_id)
        while True:

            geom_simplified = geometry.Simplify(tolerance)

            ring3 = geom_simplified.GetGeometryRef(0)
            if ring3.GetPointCount() < 100:
                print "ring3: {}, id: {}".format(ring3.GetPointCount(), geom_id)
                # print "tolerance {}".format(tolerance)
                break
            else:
               tolerance = tolerance * 10
        # print "==============="

        return geom_simplified