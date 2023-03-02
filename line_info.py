from dataclasses import dataclass
import board

@dataclass
class RL():
    chain = ['Alewife',17,16,'Davis',14,'Porter',12,11,'Harvard',9,8,'Central',6,'Kendall/MIT',4,'Charles/MGH',2,1,'Park Street','Downtown Crossing',1,'South Station',3,'Broadway',5,'Andrew',7,8,'JFK/UMass',10,11,12,13,14,15,16,'North Quincy',18,19,'Wollaston',21,22,'Quincy Center',24,25,26,'Quincy Adams',28,29,30,'Braintree']
    stations = [0, 3, 5, 8, 11, 13, 15, 18, 19, 21, 23, 25, 28, 36, 39, 42, 46, 50]
    midpoint = 18
    num_pixels = len(chain)
    data_pin = board.D6
    clock_pin = board.D13

@dataclass
class ML():
    chain = ['Savin Hill',13,14,'Fields Corner',16,'Shawmut',18,'Ashmount','Cedar Grove',21,'Butler','Milton','Central Avenue','Valley Road','Valley Road','Capen Street']
    stations = [0, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15]
    num_pixels = len(chain)
    data_pin = board.D19
    clock_pin = board.D26
    
@dataclass
class OL():
    chain = ['Oak Grove',13,'Malden Center',11,10,'Wellington',8,7,'Sullivan Square',5,'Community College',3,'North Station','Haymarket',1,'Chinatown','Tufts Medical',4,'Back Bay',6,'Massachusetts Avenue',8,'Ruggles','Roxbury Crossing',11,'Jackson Square',13,'Stony Brook',15,'Green Street',17,'Forest Hills']
    stations = [0, 2, 5, 8, 10, 12, 13, 15, 16, 18, 20, 22, 23, 25, 27, 29, 31]
    num_pixels = len(chain)
    data_pin = board.D18
    clock_pin = board.D23
    
@dataclass
class GL():
    chain = ['Medford/Tufts',16,'Ball Square',14,'Magoun Square',12,'Gilman Square','East Somerville']
    stations = [0,2,4,6,7]
    num_pixels = len(chain)
    data_pin = board.D2
    clock_pin = board.D3
    
@dataclass
class GLB():
    chain = ['Union Square',10,9,'Lechmere',7,6,'Science Park/West End',4,3,1,'Boylston','Arlington','Copely',5,6,'Hynes',8,9,'Kenmore',11,12,13,14,'Blanford Street','BU East','BU Central',18,19,'BU West','Saint Paul Street','Pleasant Street',23,'Babock Street','Packards Corner',26,'Harvard Avenue',28,'Griggs Street','Allston Street','Warren Street',32,'Washington Street','Sutherland Street',35,'Chiswick Road','Chestnut Hill Avenue','South Street',39,'Boston College']
    stations = [0, 3, 6, 10, 11, 12, 15, 18, 23, 24, 25, 28, 29, 30, 32, 33, 35, 37, 38, 39, 41, 42, 44, 45, 46, 48]
    midpoint = 9
    num_pixels = len(chain)
    data_pin = board.D4
    clock_pin = board.D17
    
@dataclass
class GLC():
    chain = ["Saint Mary's street",14,'Hawes Street','Kent Street','Saint Paul Street',18,'Coolridge Corner',20,'Summit Avenue','Brandon Hall','Fairbanks',24,'Washington Square','Tappan Street','Dean Road',28,'Engelwood Avenue','Cleveland Circle']
    stations = [0, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 16, 17]
    num_pixels = len(chain)
    data_pin = board.D27
    clock_pin = board.D22
    
@dataclass
class GLD():
    chain = [13,14,15,'Fenway','Longwood',18,'Brookline Village','Brookline Hills',21,'Beaconsfield',23,'Reservoir',25,'Chestnut Hill',26,27,'Newton Centre','Newton Highlands','Eliot',32,33,34,'Waban',36,37,'Woodland',39,'Riverside']
    stations = [3, 4, 6, 7, 9, 11, 13, 16, 17, 18, 22, 25, 27]
    num_pixels = len(chain)
    data_pin = board.D10
    clock_pin = board.D9
    
@dataclass
class GLE():
    chain = ['Prudential',7,'Symphony',9,'Northeastern',11,12,'Museum of Fine Arts','Longwood Medical',15,'Brigham Circle','Fenwood Road','Mission Park','Riverway','Back of the Hill',21,'Heath Street']
    stations = [0, 2, 4, 7, 8, 10, 11, 12, 13, 14, 16]
    num_pixels = len(chain)
    data_pin = board.D11
    clock_pin = board.D5