from mpl_toolkits.basemap import Basemap
from itp.itp_query import ItpQuery
import matplotlib.pyplot as plt
from itp.profile import Profile


path = r'D:\EOAS\ITP_package_try\itp_final_2025_01_23\itp_final_2025_01_23.db'
query = ItpQuery(path, system=[1])
results = query.fetch()

longitude = [p.longitude for p in results]
latitude = [p.latitude for p in results]

print(len(results))
# for p in results:
#     print(Profile.python_datetime(p))

m = Basemap(projection='npstere', boundinglat=70, lon_0=0, resolution='i')
m.drawcoastlines()
m.fillcontinents()
m.drawparallels(range(70, 90, 5))
m.drawmeridians(range(-180, 180, 20), latmax=85)
m.plot(longitude, latitude, latlon=True)
plt.show()


