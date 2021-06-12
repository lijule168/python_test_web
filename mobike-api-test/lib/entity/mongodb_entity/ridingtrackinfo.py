from lib.util.log_util import l


class RidingTrackInfo:
    userid = None
    orderid = None
    createdate = None
    distance = None
    carbon = None
    ridingtime = None
    cost = None
    times = None
    balance = None
    palat = None
    trackTime = None
    trackImg = None
    bikeid = None
    country = None
    home_region = None

    def __eq__(self, other):
        result = True
        if other.userid != self.userid:
            l.debug("RidingTrackInfo-userid-不一致，self({0}), other({1})".format(self.userid, other.userid))
            result = False
        if other.orderid != self.orderid:
            l.debug("RidingTrackInfo-orderid-不一致，self({0}), other({1})".format(self.orderid, other.orderid))
            result = False
        if other.createdate != self.createdate:
            l.debug("RidingTrackInfo-createdate-不一致，self({0}), other({1})".format(self.createdate, other.createdate))
            result = False
        if other.distance != self.distance:
            l.debug("RidingTrackInfo-distance-不一致，self({0}), other({1})".format(self.distance, other.distance))
            result = False
        if other.carbon != self.carbon:
            l.debug("RidingTrackInfo-carbon-不一致，self({0}), other({1})".format(self.carbon, other.carbon))
            result = False
        if other.ridingtime != self.ridingtime:
            l.debug("RidingTrackInfo-ridingtime-不一致，self({0}), other({1})".format(self.ridingtime, other.ridingtime))
            result = False
        if other.cost != self.cost:
            l.debug("RidingTrackInfo-cost-不一致，self({0}), other({1})".format(self.cost, other.cost))
            result = False
        if other.times != self.times:
            l.debug("RidingTrackInfo-times-不一致，self({0}), other({1})".format(self.times, other.times))
            result = False
        if other.balance != self.balance:
            l.debug("RidingTrackInfo-balance-不一致，self({0}), other({1})".format(self.balance, other.balance))
            result = False
        if other.palat != self.palat:
            l.debug("RidingTrackInfo-palat-不一致，self({0}), other({1})".format(self.palat, other.palat))
            result = False
        if other.trackTime != self.trackTime:
            l.debug("RidingTrackInfo-trackTime-不一致，self({0}), other({1})".format(self.trackTime, other.trackTime))
            result = False
        if other.trackImg != self.trackImg:
            l.debug("RidingTrackInfo-trackImg-不一致，self({0}), other({1})".format(self.trackImg, other.trackImg))
            result = False
        if other.bikeid != self.bikeid:
            l.debug("RidingTrackInfo-bikeid-不一致，self({0}), other({1})".format(self.bikeid, other.bikeid))
            result = False
        if other.country != self.country:
            l.debug("RidingTrackInfo-country-不一致，self({0}), other({1})".format(self.country, other.country))
            result = False
        if other.home_region != self.home_region:
            l.debug("RidingTrackInfo-home_region-不一致，self({0}), other({1})".format(self.home_region, other.home_region))
            result = False
        return result

    def __ne__(self, other):
        return  not self.__eq__(other)