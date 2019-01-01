from bs4 import BeautifulSoup
import urllib2
import requests
import time
from Queue import Queue
from threading import Thread
from random import random
import string
import sqlite3 as lite
import socket
import httplib
import ssl
# used for proxy
#import os
# set run ID, Colon, State Tag, Cities, Proxy,

#RunID = 'NY:New_York:Queens:'
#RunID = 'Phoenix'
#RunID = 'NY:New_York:Brooklyn:'
#RunID = 'Miami'
#RunID = 'Miami1'
#RunID = 'Jacksonville'
#RunID = 'Jacksonville1'
#RunID = 'Tampa'
#RunID = 'Tampa1'
#RunID = 'Dallas'
#RunID = 'Houston'
#RunID = 'Fort_Worth'
#RunID = 'San Antonio'
#RunID = 'Atlanta'
#RunID = 'Indianapolis'
#RunID = 'Portland'
#RunID = 'Charlotte'
#RunID = 'Denver'
#RunID = 'Columbus'
#RunID = 'Washington_D.C.'
#RunID = 'Nashville'
#RunID = 'Oklahoma_City'
#RunID = 'Milwaukee'
#RunID = 'Louisville'
#RunID = 'Albuquerque'
#RunID = 'New_Orleans'
RunID = 'Detroit'
Date = (time.strftime("%d/%m/%Y"))

####### Cities
doubleColon = False
# state tag begins after p:
#StateTag = 'TX:Austin::'
#StateTag = 'TX:Dallas::'
#StateTag = 'TX:Fort_Worth::'
#StateTag = 'TX:San_Antonio::'
#StateTag = 'GA:Atlanta::'
#StateTag = 'IN:'
#StateTag = 'OR:Portland::'
#StateTag = 'NC:Charlotte::'
#StateTag = 'CO:Denver::'
#StateTag = 'OH:Columbus::'
#StateTag = 'DC:Washington::'
#StateTag = 'TN:'
#StateTag = 'OK:'
#StateTag = 'FL:'
#StateTag = 'WI:'
#StateTag = 'KY:'
#StateTag = 'NM:Albuquerque::'
#StateTag = 'LA:'
StateTag = 'MI:Detroit::'
#Cities = 'Anthem::,Apache_Junction::,Avondale::,Buckeye::,Carefree::,Casa_Grande::,Cave_Creek::,Chandler::,Coolidge::,El_Mirage::,Florence::,Fountain_Hills::,Gilbert::,Glendale::,Gold_Canyon::,Goodyear::,Laveen::,Litchfield_Park::,Maricopa::,Mesa::,Paradise_Valley::,Payson::,Peoria::,Phoenix::,Queen_Creek::,San_Tan_Valley::,Scottsdale::,Sun_City::,Sun_City_West::,Sun_Lakes::,Surprise::,Tempe::,Tolleson::,Youngtown::'
#StateTag = 'NY:New_York:Queens:'
#StateTag = 'NY:New_York:Brooklyn:'
#Cities = 'Arverne,Astoria,Astoria_Heights,Auburndale,Bay_Terrace,Bayside,Beechurst,Bellaire,Belle_Harbor,Bellerose,Breezy_Point,Briarwood,Cambria_Heights,College_Point,Corona,Douglaston,Downtown_Flushing,East_Elmhurst,Edgemere,Elmhurst,Far_Rockaway,Floral_Park,Flushing,Flushing_Meadows,Forest_Hills,Fresh_Meadows,Glen_Oaks,Glendale,Hillcrest,Hollis,Holliswood,Howard_Beach,Hunters_Point,JFK_Airport,Jackson_Heights,Jamaica,Jamaica_Estates,Jamaica_Hills,Kew_Gardens,Kew_Gardens_Hills,LaGuardia_Airport,Laurelton,Lindenwood,Little_Neck,Long_Island_City,Malba,Maspeth,Middle_Village,Murray_Hill,North_Corona,Oakland_Gardens,Ozone_Park,Pomonok,Queens_Village,Queensborough_Hill,Rego_Park,Richmond_Hill,Ridgewood,Rochdale,Rockaway_Park,Rosedale,Seaside,Somerville,Springfield_Gardens,Steinway,Sunnyside,Utopia,Whitestone,Woodhaven,Woodside'
#Cities = 'Baychester,Bedford_Park,Belmont,Castle_Hill,City_Island,Claremont_Village,Clason_Point,Co-op_City,Concourse,Concourse_Village,Country_Club,East_Tremont,Eastchester,Edenwald,Edgewater_Park,Fieldston,Fordham,High_Bridge,Hunts_Point,Kingsbridge,Longwood,Melrose,Morris_Heights,Morris_Park,Morrisania,Mott_Haven,Mount_Eden,Mount_Hope,North_Riverdale,Norwood,Olinville,Parkchester,Pelham_Bay,Pelham_Gardens,Port_Morris,Riverdale,Schuylerville,Soundview,Spuyten_Duyvil,Throgs_Neck,Unionport,University_Heights,Van_Nest,Wakefield,West_Farms,Westchester_Square,Williamsbridge,Woodlawn'
# Brooklyn
#Cities = 'Bath_Beach,Bay_Ridge,Bedford_Stuyvesant,Bensonhurst,Bergen_Beach,Boerum_Hill,Borough_Park,Brighton_Beach,Brooklyn_Heights,Brownsville,Bushwick,Canarsie,Carroll_Gardens,City_Line,Clinton_Hill,Cobble_Hill,Columbia_Street_Waterfront_District,Coney_Island,Crown_Heights,Cypress_Hills,DUMBO,Ditmas_Park,Downtown_Brooklyn,Dyker_Heights,East_Flatbush,East_New_York,East_Williamsburg,Flatbush,Flatlands,Fort_Greene,Fort_Hamilton,Georgetown,Gerritson_Beach,Gowanus,Gravesend,Greenpoint,Highland_Park,Kensington,Manhattan_Beach,Marine_Park,Midwood,Mill_Basin,Mill_Island,New_Lots,Ocean_Hill,Ocean_Parkway,Paedergat_Basin,Park_Slope,Prospect_Heights,Prospect_Lefferts_Gardens,Prospect_Park,Red_Hook,Remsen_Village,Sea_Gate,Sheepshead_Bay,South_Slope,South_Williamsburg,Spring_Creek,Starret_City,Sunset_Park,Vinegar_Hill,Weeksville,Williamsburg_-_North_Side,Williamsburg_-_South_Side,Windsor_Terrace,Wingate'
#Cities = 'Allapattah,Bay_Point,Bayside,Belle_Meade,Brickell,Buena_Vista,Civic_Center,Coconut_Grove,Coral_Gate,Design_District,Downtown,Edgewater,Flagami,Grapeland_Heights,Liberty_City,Little_Haiti,Little_Havana,Little_River,Lummus_Park,Magnolia_Park,MiMo_District,Midtown,Morningside,Omni,Overtown,Park_West,Shenandoah,Shorecrest,Silver_Bluff,The_Roads,West_Flagler,Wynwood'
#Cities = 'Coral_Gables::,Doral::,Fort_Lauderdale::,Hialeah::,Hialeah_Gardens::,Key_Biscayne::,Miami::,Miami_Beach::,Miami_Shores::,Miami_Springs::,North_Bay_Village::,South_Miami::,West_Miami::,Wilton_Manors::'
#Cities = 'Avondale,Beaches,Downtown,Eastside,Greater_Arlington,LaVilla,Mandarin,Northside,Ortega,Riverside,San_Marco,Southbank,Southside,St._Nicholas,Westside'
#Cities = 'Atlantic_Beach::,Callahan::,Fernandina_Beach::,Fleming_Island::,Fruit_Cove::,Green_Cove_Springs::,Jacksonville::,Jacksonville_Beach::,Middleburg::,Neptune_Beach::,Orange_Park::,Palm_Valley::,Ponte_Vedra::,Ponte_Vedra_Beach::,Saint_Augustine::,Saint_Johns::,St._Augustine::,Yulee::'
#Cities = 'Apollo_Beach,Belleair,Brandon,Busch_Gardens,Carrollwood,Channelside,Citrus_Park,Clearwater,Clearwater_Beach,Davis_Islands,Dover,Downtown_St._Petersburg,Downtown_Tampa,Dunedin,Feather_Sound,Gateway,Gibsonton,Grand_Central_District,Gulfport,Harbour_Island,Holiday,Hyde_Park,Indian_Rocks_Beach,Interbay,International,Kenneth_City,Land_O%27_Lakes,Largo,Lithia,Lutz,MacDill_AFB,Madeira-Redington,Mango,Midtown,New_Port_Richey,New_Tampa,Odessa,Old_South_East,Oldsmar,Palm_Harbor,Palma_Ceia,Pinellas_Park,Riverview,Ruskin,Safety_Harbor,Seffner,Seminole,Seminole_Heights,SoHo,South_Bayshore,South_Pasadena,South_St._Petersburg_-_Edit,South_Tampa,St_Pete_Beach,Sun_City,Tampa_Palms,Tarpon_Springs,Temple_Terrace,Tierra_Verde,Town_N_Country,Treasure_Island,Trinity,Tyrone,USF,Valrico,Wesley_Chapel,West_Tampa,Westshore,Wimauma,Ybor_City'
#Cities = 'Belleair_Bluffs::,Dade_City::,Hudson::,Land_O_Lakes::,Madeira_Beach::,Plant_City::,Port_Richey::,Saint_Petersburg::,San_Antonio::,St._Pete_Beach::,St._Petersburg::,St_Petersburg::,Sun_City_Center::,Tampa::,Tampa_Bay::,Thonotosassa::,Town_%27n%27_Country::,Zephyrhills::'
#Cities = '2nd_Street_District,78704_(South_Austin),Allandale,Arboretum,Barrington_Oaks,Barton_Hills,BattleBend_Springs,Bouldin_Creek,Brentwood,Bryker_Woods,Cat_Mountain,Cherry_Creek,Cherrywood,Circle_C_Ranch,Clarksville,Copperfield,Crestview,Downtown,East_Austin,Far_West/Northwest_Hills,French_Place,Gracy_Woods,Great_Hills,Harris_Branch,Hyde_Park,Lamplight_Village,Market_District,Milwood,Northwest_Austin,Old_Enfield,Oltorf/East_Riverside,Onion_Creek,Pflugerville,Rollingwood,Rosedale,Shady_Hollow,Sixth_Street_District,So-Fi_(S._1st_St._District),SoCo_(S._Congress_Ave.),South_Lamar_District,Southeast_Austin,Spyglass/Bartons_Bluff,Tarryton/Exposition_Blvd.,The_Drag,Town_Lake,Travis_Heights,University_of_Texas,Warehouse_District,Wells_Branch,West_Campus,Westlake_Hills'
#Cities = 'Addison,Bishop_Arts_District,Carrollton,Deep_Ellum,Design_District,Downtown,East_Dallas,Exposition_Park,Fair_Park,Farmer%27s_Branch,Highland_Park,Lake_Highlands,Lakewood,Lower_Greenville,North_Dallas,Northeast_Dallas,Oak_Cliff,Oak_Lawn,South_Dallas,University_Park,Upper_Greenville,Uptown,Victory_Park'
#Cities = 'Acres_Homes,Addicks/Park_Ten,Alief,Bellaire,Braeburn,Braeswood_Place,Carverdale,Central_Southwest,Chinatown,Clear_Lake,Clinton_Park/Tri-Community,Denver_Harbor/Port_Houston,Downtown,EaDo,East_Houston,East_Little_York/Homestead,Eastex/Jensen,Eastwood,Edgebrook,El_Dorado/Oates_Prairie,Energy_Corridor,Fairbanks/Northwest_Crossing,Fifth_Ward,Fondren_Gardens,Fondren_Southwest,Fort_Bend_Houston,Fourth_Ward,Galleria/Uptown,Golfcrest/Belfort/Reveille,Greenspoint,Greenway,Gulfgate/Pine_Valley,Gulfton,Harrisburg/Manchester,Hidden_Valley,Highland_Village,Hobby,Hunterwood,IAH_Airport_Area,Independence_Heights,Inwood,Kashmere_Gardens,Kingwood,Lake_Houston,Langwood,Lawndale/Wayside,Lazy_Brook/Timbergrove,MacGregor,Magnolia_Park,Meadowbrook/Allendale,Medical_Center,Memorial,Meyerland,Midtown,Minnetex,Montrose,Museum_District,Northshore,Northside/Northline,Northside_Village,Oak_Forest/Garden_Oaks,Old_Spanish_Trail/South_Union,Park_Place,Pecan_Park,Pleasantville,Rice_Military,River_Oaks,Second_Ward,Settegast,Sharpstown,Sixth_Ward,South_Acres/Crestmont_Park,South_Belt/Ellington,South_Main,South_Park,Spring_Branch,Sunnyside,The_Heights,Third_Ward,Trinity/Houston_Gardens,Upper_Kirby,Warehouse_District,Washington_Corridor,West_Branch,West_Oaks,West_University,Westbury,Westchase,Westwood,Willow_Meadows/Willowbend,Willowbrook'
#Cities = 'Arlington_Heights,Downtown,Eastside,Far_North,Far_Northwest,Far_South,Far_Southwest,Far_West,Northeast,Northside,South_East,Southside,Sycamore,TCU/West_Cliff,Wedgwood,Western_Hills/Ridglea'
#Cities = 'Alamo_Heights,Alta_Vista,Beacon_Hill,Castle_Hills,Dellview,Downtown,Eastside,Five_Points,Government_Hill,King_William,Lavaca,Los_Angeles_Heights,Lower_Southeast_Side,Mahncke_Park,Medical_Center,Monte_Vista,Monticello_Park,Oak_Park/Northwood,Olmos_Park,Olmos_Park_Terrace,Shavano_Park,South_Side,Southtown,Stone_Oak,Terrell_Heights,Terrell_Hills,Tobin_Hill,Wilshire,Wilshire_Terrace,Windcrest,Woodlawn_Lake'
#Cities = 'Ansley_Park,Atlantic_Station,Brookhaven,Buckhead,Cabbagetown,Candler_Park,Castleberry_Hill,Centennial_Place,Decatur,Downtown,Druid_Hills,East_Atlanta_Village,East_Lake,Edgewood,Emory_Village,Georgia_Tech,Grant_Park,Inman_Park,Kirkwood,Lake_Claire,Lindbergh,Little_Five_Points,Midtown,Morningside_/_Lenox_Park,Old_Fourth_Ward,Ormewood_Park,Poncey-Highland,Reynoldstown,Vinings,Virginia_Highland,West_End,West_Paces_Ferry_/_Northside,Westside_/_Home_Park'
#Cities = 'Avon::,Bargersville::,Beech_Grove::,Brownsburg::,Camby::,Carmel::,Danville::,Fishers::,Franklin::,Greenfield::,Greenwood::,Indianapolis::,Lebanon::,Mc_Cordsville::,Mooresville::,New_Palestine::,Noblesville::,Pendleton::,Plainfield::,Shelbyville::,Speedway::,Westfield::,Whiteland::,Whitestown::,Zionsville::'
#Cities = 'Alberta_Arts_District,Alphabet_District,Arbor_Lodge,Argay,Beaumont_-_Wilshire,Belmont,Boise,Brentwood_-_Darlington,Broadway_District,Brooklyn,Buckman,Cathedral_Park,Centennial,Central_Eastside,Clinton,Concordia,Creston-Kenilworth,Cully,Downtown,Eliot,Foster-Powell,Goose_Hollow,Grant_Park,Hawthorne,Hayden_Island,Hazelwood,Hillsdale,Hollywood,Hosford-Abernethy,Humboldt,Industrial_District,Irvington,Kenton,Kerns,King,Ladd%27s_Addition,Lents,Lloyd_District,Lower_Burnside,Mill_Park,Mississippi,Montavilla,Mt._Scott_-_Arleta,Mt._Tabor,Multnomah_Village,North_Portland,North_Tabor_-_Center,Northeast_Portland,Northwest,Old_Town_-_Chinatown,Overlook,Parkrose,Parkrose_Heights,Pearl_District,Piedmont,Pleasant_Valley,Portsmouth,Powellhurst_-_Gilbert,Richmond,Rose_City_Park,Roseway,Sabin,Sellwood,South_Portland,South_Tabor,Southeast_Portland,Southwest_Portland,St._Johns,Sullivan%27s_Gulch,Sunnyside,University_Park,Vernon,Woodlawn,Woodstock'
#Cities = 'Arboretum,Ballantyne,Biddleville,Cotswold,Derita,Dilworth,Eastland,Elizabeth,First_Ward,Fourth_Ward,Highland_Creek,Myers_Park,NoDa,North_Charlotte,Paw_Creek,Plaza_Midwood,Quail_Hollow,Sedgefield,Sherwood_Forest,South_End,South_Park,Starmount,Steele_Creek,Third_Ward,University_City,Uptown,Villa_Heights'
#Cities = 'Alamo_Placita,Auraria,Baker,CBD,Capitol_Hill,Cherry_Creek,City_Park,Congress_Park,Country_Club,Curtis_Park,Five_Points,Golden_Triangle,Highland,Jefferson_Park,Lincoln_Park,Lodo,Northeast,Northwest,Park_Hill,Southeast,Southwest,Speer,Stapleton,University,University_Park,Uptown,Washington_Park,Washington_Park_West'
#Cities = 'Arena_District,Bexley,Brewery_District,Clintonville,Crosswoods,Discovery_District,Downtown,Driving_Park,Eastmoor,Easton,Franklinton,Gahanna,German_Village,Grandview_Heights,Harrison_West,Hilltop,Italian_Village,King-Lincoln,Linden,Merion_Village,Northland,Northwest,Olde_Towne_East,Polaris,Schumacher_Place,Short_North,Southeast,Southside,University_District,Upper_Arlington,Victorian_Village,Whitehall,Worthington'
#Cities = 'Adams_Morgan,American_University_Park,Anacostia,Barney_Circle,Barry_Farm,Bloomingdale,Brentwood,Brightwood,Brookland,Burleith,Capitol_Hill,Carver/Langston,Chevy_Chase,Chinatown,Cleveland_Park,Columbia_Heights,Crestwood,Deanwood,Dupont_Circle,Eckington,Edgewood,Federal_Triangle,Foggy_Bottom,Fort_Totten,Foxhall,Friendship_Heights,Gateway,Georgetown,Glover_Park,H_Street_Corridor/Atlas_District/Near_Northeast,Hillcrest,Ivy_City,Kalorama,Kingman_Park,Langdon_Park,Le_Droit_Park,Lincoln_Park,Logan_Circle,Michigan_Park,Mount_Pleasant,Mount_Vernon_Square,Navy_Yard,NoMa,Palisades,Park_View,Penn_Quarter,Petworth,Pleasant_Plains,Queens_Chapel,Shaw,Shepherd_Park,Southeast,Spring_Valley,Takoma,Tenleytown,Trinidad,U_Street_Corridor,Van_Ness/Forest_Hills,Wesley_Heights,West_End,Woodley_Park'
#Cities = 'Antioch::,Ashland_City::,Brentwood::,Fairview::,Franklin::,Gallatin::,Goodlettsville::,Greenbrier::,Hendersonville::,Hermitage::,Joelton::,Kingston_Springs::,La_Vergne::,Lebanon::,Madison::,Mount_Juliet::,Mt._Juliet::,Murfreesboro::,Nashville::,Nolensville::,Old_Hickory::,Pleasant_View::,Smyrna::,White_House::,Whites_Creek::'
#Cities = 'Del_City::,Nichols_Hills::,Oklahoma_City::,Warr_Acres::,Yukon::'
#Cities = 'Clermont::,Davenport::,DeBary::,Debary::,Deltona::,Eustis::,Heathrow::,Leesburg::,Minneola::,Mount_Dora::,Orlando::,Saint_Cloud::,Sorrento::,St._Cloud::,Tavares::'
#Cities = 'Brookfield::,Butler::,Cedarburg::,Cudahy::,Elm_Grove::,Fox_Point::,Franklin::,Germantown::,Glendale::,Grafton::,Greendale::,Greenfield::,Hales_Corners::,Hartford::,Hartland::,Hubertus::,Menomonee_Falls::,Menomonee_Fls::,Mequon::,Milwaukee::,Mukwonago::,Muskego::,New_Berlin::,Oak_Creek::,Pewaukee::,Racine::,Saint_Francis::,Slinger::,South_Milwaukee::,Sussex::,Thiensville::,Waterford::,Waukesha::,West_Milwaukee::,Whitefish_Bay::'
#Cities = 'Crestwood::,La_Grange::,Louisville::,Mount_Washington::,Pewee_Valley::,Shelbyville::,Shepherdsville::,Shively::,Simpsonville::,Taylorsville::'
#Cities = 'Airport/Base,Barelas/South_Valley,Business_Parkway/Academy_Acres,Downtown,Eastside,International_District,Midtown/University,Nob_Hill,North_Valley/Los_Ranchos,Old_Town,Uptown,Westside'
#Cities = 'Arabi::,Belle_Chasse::,Chalmette::,Lafitte::,Luling::,Mandeville::,New_Orleans::,Pearl_River::,Slidell::,Violet::'
Cities = 'Bagley,Bricktown,Cass_Corridor,Chandler_Park,Corktown,Cultural_Center,Delray,Depot_Town_Ypsilanti,Downriver,Downtown_Ann_Arbor,Downtown_Berkley,Downtown_Birmingham,Downtown_Clawson,Downtown_Dearborn,Downtown_Detroit,Downtown_Ferndale,Downtown_Hamtramck,Downtown_Mount_Clemens,Downtown_Pontiac,Downtown_Rochester,Downtown_Royal_Oak,Downtown_Saint_Clair_Shores,Downtown_Wyandotte,Downtown_Ypsilanti,Eastern_Market,Greektown,Indian_Village,Kerrytown_Ann_Arbor,Mexicantown,Midtown,New_Center,Normal_Park_Ypsilanti,South_University_Ann_Arbor,Southwest_Detroit,The_Village/Downtown_Grosse_Pointe,Warrendale,Wayne_State,Woodbridge'
Cities = Cities.split(",")

####### Initialization
CityLink = {}
ID_database = {}
propertyholder = {}
ind = 0
HTTP_RETRIES = 5
HTTP_TIMEOUT = 5
socket.setdefaulttimeout(HTTP_TIMEOUT)
start_time = time.time()
pageNums = {}

# proxy
# proxy = '204.29.115.149:8080'
# os.environ['http_proxy'] = proxy
# os.environ['https_proxy'] = proxy
#
# proxy = urllib2.ProxyHandler({'http': proxy, 'https': proxy})
# opener = urllib2.build_opener(proxy)
# urllib2.install_opener(opener)

# Handles crashes so it doesn't repeat duplicate scrapes
con = lite.connect('SQL_YelpSalons.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT DISTINCT Location FROM YelpSalons WHERE (RunID = ?)", (RunID,))
    citycomplete = cur.fetchall()

    ## remove bad data
    length = int(len(citycomplete)) - 1
    if len(citycomplete) > 0:
        for row in xrange(length):
            print row
        print 'done'
        print citycomplete[length]
        bad_data = citycomplete[length]
        bad_data = ''.join(bad_data)
        bad_data = str(bad_data)
        cur.execute("DELETE FROM YelpSalons WHERE (Location = ?)", (bad_data,))

    cur.execute("SELECT DISTINCT Location FROM YelpSalons WHERE (RunID = ?)", (RunID,))
    citycomplete = cur.fetchall()

    for row in citycomplete:
        row = ''.join(row)
        if doubleColon:
            row = str(row) + "::"
        else:
            row = str(row)
        if row in Cities:
            Cities.remove(row)

print "Cities left ", (len(Cities))
print list(Cities)
city_queue = Queue(len(Cities))
city_out_queue = Queue(0)

for row in range(len(Cities)):
    city_queue.put(row)


####### Wait time
def waitTime():
    wait = random() / 2 + 5
    time.sleep(wait)


####### Get HTML def
def readHTML(weblink):
    attempt = 0
    while attempt < HTTP_RETRIES:
        attempt += 1
        wait = random() / 2 + attempt - 1 + .25
        time.sleep(wait)
        try:
            request = urllib2.Request(weblink)
            response = urllib2.urlopen(request, timeout=4)
            r = response.read()
            break
        except urllib2.HTTPError, e:
            print e.reason
            continue
        except urllib2.URLError, f:
            print f.reason
            continue
        except httplib.HTTPException:
            print "Rare Error"
            continue
        except ValueError:
            continue
        except ssl.SSLError:
            continue

    return attempt, r


def CityYelp():
    while True:
        cityid = city_queue.get()
        CityLink = "https://www.yelp.com/search?find_desc=hair+salons&start=0&l=p:" + StateTag + "[" + Cities[
            cityid] + "]"
        attempt, r = readHTML(CityLink)
        if attempt >= 4:
            city_queue.task_done()
            print "page error"
            break
        soup = BeautifulSoup(r)
        waitTime()
        pages = soup.find_all("div", class_="page-of-pages arrange_unit arrange_unit--fill")
        try:
            pages = pages[0].get_text()
            pages = pages.strip()
            pageNums = int(pages.split("Page 1 of", 1)[1])
        except:
            pageNums = 1
        print pageNums
        if pageNums > 70:
            pageNums = 70
        CityTag = Cities[cityid]
        city_out_queue.put((CityTag, pageNums))
        city_queue.task_done()


for i in xrange(10):
    t = Thread(target=CityYelp)
    t.daemon = True
    t.start()

city_queue.join()
cityPageData = list(city_out_queue.queue)

####### loop through all cities
for count in xrange(len(cityPageData)):
    ####### reinitializes
    ID_database = {}
    propertyholder = {}
    test = {}
    pages = {}
    row = {}
    #######
    currentCity = cityPageData[count]
    print currentCity
    City_URL = currentCity[0]
    if doubleColon:
        Location = City_URL[:-2]
    else:
        Location = City_URL
    pages = currentCity[1]
    index_queue = Queue(pages)
    index_output = Queue(0)

    for row in range(pages):
        index_queue.put(row)


    def getindex():
        while not index_queue.empty():
            try:
                page = index_queue.get()  # add timeout=20 if more problems occur
            except ssl.SSLError:
                index_queue.task_done()
                print "ssl error"
                break
            except:
                print "empty queue error"
                index_queue.task_done()
                break
            print page
            pagestr = str(page)

            if not pagestr:
                print "empty page"
                print page
                index_queue.task_done()
                break

            if page == 0:
                pagestr = '0'
                weblink = 'https://www.yelp.com/search?find_desc=hair+salons&start=0&l=p:' + StateTag + '[' + City_URL + ']'
            else:
                weblink = 'https://www.yelp.com/search?find_desc=hair+salons&start=' + pagestr
                weblink = weblink + '0&l=p:' + StateTag + '[' + City_URL + ']'

            attempt, r = readHTML(weblink)

            if attempt >= 4:
                index_queue.task_done()
                break

            waitTime()
            soup = BeautifulSoup(r)
            waitTime()
            propertyids = soup.find_all("a", class_="biz-name js-analytics-click")

            if not propertyids:
                print "empty"
                print propertyids
                index_queue.task_done()
                break

            loopcount = len(propertyids)

            for x in range(loopcount):
                if x == 0:
                    pass
                else:
                    try:
                        index_output.put(propertyids[x].attrs['href'])
                    except:
                        print "Rare index error"
                        index_queue.task_done()
                        break
            index_queue.task_done()

            # Start a pool of X workers


    for i in xrange(10):
        t = Thread(target=getindex)
        t.daemon = True
        t.start()
        t.join(30)
        print 't.isAlive()', t.isAlive()
        t.join()

    index_queue.join()
    print "part " + str(count) + " complete"
    index_results = list(index_output.queue)
    print "debug below"
    debug = list(index_queue.queue)
    print debug
    listingcount = len(index_results)
    url_queue = Queue(listingcount)
    output_addresses = Queue(listingcount)
    output_phone = Queue(listingcount)
    output_website = Queue(listingcount)
    output_yelp = Queue(listingcount)

    # Change this to read your links and queue them for processing
    for url in range(listingcount):
        websitelink = "https://www.yelp.com" + str(index_results[url])
        url_queue.put(websitelink)


    def worker():
        '''Gets the next url from the queue and processes it'''
        while not url_queue.empty():

            url = url_queue.get()
            print url

            attempt, r = readHTML(url)
            if attempt >= 4:
                url_queue.task_done()
                print "attempt failed in worker"
                break

            waitTime()
            soup = BeautifulSoup(r)

            Address = soup.find_all('strong', class_="street-address")
            try:
                Address = Address[0].get_text()
                Address = Address.strip()
            except:
                Address = "None"
                pass

            Phone = soup.find_all('span', class_="biz-phone")
            try:
                Phone = Phone[0].get_text()
                Phone = Phone.strip()
            except:
                Phone = "None"
                pass

            Website = soup.find_all('span', class_="biz-website js-add-url-tagging")
            try:
                Website = Website[0].a.get_text()
            except:
                Website = "None"
                pass

            output_addresses.put(Address)
            output_phone.put(Phone)
            output_website.put(Website)
            output_yelp.put(url)

            url_queue.task_done()


    # Start a pool of X workers
    for i in xrange(10):
        t = Thread(target=worker)
        t.daemon = True
        t.start()
        t.join(30)
        print 't.isAlive()', t.isAlive()
        t.join()

    # Block until everything is finished.
    url_queue.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    addresses_results = list(output_addresses.queue)
    phone_results = list(output_phone.queue)
    website_results = list(output_website.queue)
    yelp_results = list(output_yelp.queue)
    listingcount = len(addresses_results)

    con = lite.connect('SQL_YelpSalons.db')
    cur = con.cursor()

    for q in range(listingcount):

        with con:
            Yelp_Link = "https://www.yelp.com" + str(index_results[q])
            Address = addresses_results[q]
            Number = phone_results[q]
            if website_results[q] == "None":
                Website = website_results[q]
            else:
                Website = "http://www." + website_results[q]

            cur.execute("INSERT INTO YelpSalons VALUES(?, ?, ?, ?, ?, ?, ?)",
                        (Yelp_Link, Address, Number, Website, Location, Date, RunID))
