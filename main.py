import core.reversegeocoder as rg
import utils.csvtools as MonkeyWriter

if __name__ == "__main__":
    rg = rg.reverseGeocoder()
    lat = 40.714224
    lon = -73.961452
    address = rg.get_address(lat, lon)
    print(address)
    rg.close()