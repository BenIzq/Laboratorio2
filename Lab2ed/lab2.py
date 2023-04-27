from typing import List, Dict


class IPlace:
    def __init__(self, address: str, price: float, contact_phone: str, id: str):
        self.address = address
        self.price = price
        self.contact_phone = contact_phone
        self.id = id


class House(IPlace):
    def __init__(self, address: str, price: float, contact_phone: str, id: str, zone_dangerous: str):
        super().__init__(address, price, contact_phone, id)
        self.zone_dangerous = zone_dangerous


class Apartment(IPlace):
    def __init__(self, address: str, price: float, contact_phone: str, id: str, is_pet_friendly: bool):
        super().__init__(address, price, contact_phone, id)
        self.is_pet_friendly = is_pet_friendly


class Premise(IPlace):
    def __init__(self, address: str, price: float, contact_phone: str, id: str, commercial_activities: List[str]):
        super().__init__(address, price, contact_phone, id)
        self.commercial_activities = commercial_activities


def is_pet_friendly(x: bool, y: float, budget: float, wants_pet_friendly: bool) -> bool:
    return x == wants_pet_friendly and y <= budget


def is_ok_danger(x: str, y: float, budget: float, wants_danger: str) -> bool:
    if wants_danger == "Green":
        return do_somenting_green(x) and y <= budget
    elif wants_danger == "Yellow":
        return do_somenting_yellow(x) and y <= budget
    elif wants_danger == "Orange":
        return do_somenting_orange(x) and y <= budget
    else:
        return do_somenting_red(x) and y <= budget


def is_pymes_allow(x: List[str], y: float, budget: float, wants_pymes: str) -> bool:
    return wants_pymes in x and y <= budget


def filter_a(numbers: List[Apartment], budget: float, wants_pet_friendly: bool, callback_a) -> Dict[str, float]:
    results_apartments = {}
    for number in numbers:
        if callback_a(number.is_pet_friendly, number.price, budget, wants_pet_friendly):
            results_apartments[number.id] = number.price
    return results_apartments


def filter_h(numbers: List[House], budget: float, wants_danger: str, callback_h) -> Dict[str, float]:
    results_houses = {}
    for number in numbers:
        if callback_h(number.zone_dangerous, number.price, budget, wants_danger):
            results_houses[number.id] = number.price
    return results_houses


def filter_p(numbers: List[Premise], budget: float, wants_pymes: str, callback_p) -> Dict[str, float]:
    results_premises = {}
    for number in numbers:
        if callback_p(number.commercial_activities, number.price, budget, wants_pymes):
            results_premises[number.id] = number.price
    return results_premises


def do_somenting_green(color: str) -> bool:
    return color in {"Green", "Yellow", "Orange", "Red"}


def do_somenting_yellow(color: str) -> bool:
    return color in {"Yellow", "Orange", "Red"}


def do_somenting_orange(color: str) -> bool:
    return color in {"Orange"}

class IPlace:
  def init(self, address, price, contactPhone, id):
    self.address = address
    self.price = price
    self.contactPhone = contactPhone
    self.id = id

class House(IPlace):
  def init(self, address, price, contactPhone, id, zoneDangerous):
    super().init(address, price, contactPhone, id)
    self.zoneDangerous = zoneDangerous

class Apartment(IPlace):
  def init(self, address, price, contactPhone, id, isPetFriendly):
    super().init(address, price, contactPhone, id)
    self.isPetFriendly = isPetFriendly

class Premise(IPlace):
  def init(self, address, price, contactPhone, id, commercialActivities):
    super().init(address, price, contactPhone, id)
    self.commercialActivities = commercialActivities

def filterA(numbers, budget, wantsPetFriendly, callback):
  results = {}
  for number in numbers:
    if callback(number.isPetFriendly, number.price, budget, wantsPetFriendly):
      results[number.id] = number.price
  return results

def filterH(numbers, budget, wantsDanger, callback):
  results = {}
  for number in numbers:
    if callback(number.zoneDangerous, number.price, budget, wantsDanger):
      results[number.id] = number.price
  return results

def filterP(numbers, budget, wantsPymes, callback):
  results = {}
  for number in numbers:
   if callback(number.commercialActivities, number.price, budget, wantsPymes):
    results[number.id] = number.price
  return results

def isPetFriendly(x, y, budget, wantsPetFriendly):
  return x == wantsPetFriendly and y <= budget

def isOkDanger(x, y, budget, wantsDanger):
  if wantsDanger == "Green":
    return doSomentingGreen(x) and y <= budget
  elif wantsDanger == "Yellow":
    return doSomentingYellow(x) and y <= budget
  elif wantsDanger == "Orange":
    return doSomentingOrange(x) and y <= budget
  else:
    return doSomentingRed(x) and y <= budget

def isPymesAllow(x, y, budget, wantsPymes):
  return wantsPymes in x and y <= budget

def doSomentingGreen(color):
  if color == "Green" or color == "Yellow" or color == "Orange" or color == "Red":
    return True
  else:
    return False

def doSomentingYellow(color):
  if color == "Yellow" or color == "Orange" or color == "Red":
    return True
  else:
    return False

def doSomentingOrange(color):
  if color == "Orange" or color == "Red":
    return True
  else:
    return False

def doSomentingRed(color):
  if color == "Red":
    return True
  else:
    return False

def main(input2, houses, apartments, premises):
  resultsHouses = filterH(houses, input2["budget"], input2["minDanger"], isOkDanger)
  resultsApartments = filterA(apartments, input2["budget"], input2["wannaPetFriendly"], isPetFriendly)

  def doSomentingGreen(color):
        if color == "Green":
            return True
        elif color == "Yellow":
            return True
        elif color == "Orange":
            return True
        elif color == "Red":
            return True
        else:
            return False

  def doSomentingYellow(color):
        if color == "Yellow":
            return True
        elif color == "Orange":
            return True
        elif color == "Red":
            return True
        else:
            return False

  def doSomentingOrange(color):
        if color == "Orange":
            return True
        elif color == "Red":
            return True
        else:
            return False

  def doSomentingRed(color):
        if color == "Red":
            return True
        else:
            return False


  class IPlace:
        def __init__(self):
            self.address = ""
            self.price = 0.0
            self.contactPhone = ""
            self.id = ""

  class House(IPlace):
        def __init__(self):
            super().__init__()
            self.zoneDangerous = ""

  class Apartment(IPlace):
        def __init__(self):
            super().__init__()
            self.isPetFriendly = False

  class Premise(IPlace):
        def __init__(self):
            super().__init__()
            self.commercialActivities = []


  def FilterA(numbers, budget, wantsPetFriendly, callback):
        resultsApartments = {}
        for number in numbers:
            if callback(number.isPetFriendly, number.price, budget, wantsPetFriendly):
                resultsApartments[number.id] = number.price
        return resultsApartments


  def FilterH(numbers, budget, wantsDanger, callback):
        resultsHouses = {}
        for number in numbers:
            if callback(number.zoneDangerous, number.price, budget, wantsDanger):
                resultsHouses[number.id] = number.price
        return resultsHouses


  def FilterP(numbers, budget, wantsPymes, callback):
        resultsPremises = {}
        for number in numbers:
            if callback(number.commercialActivities, number.price, budget, wantsPymes):
                resultsPremises[number.id] = number.price
        return resultsPremises


  def Main():
        input2 = {
            "requiredServices": [],
            "typeBuilder": "",
            "minDanger": "",
            "wannaPetFriendly": False,
            "commercialActivity": "",
            "budget": 0.0
        }

        resultsApartments = {}
        resultsHouses = {}
        resultsPremises = {}

        def IsPetFriendly(x, y, budget, wantsPetFriendly):
            return x == wantsPetFriendly and y <= budget

        def IsOkDanger(x, y, budget, wantsDanger):
            if wantsDanger == "Green":
                return doSomentingGreen(x) and y <= budget
            elif wantsDanger == "Yellow":
                return doSomentingYellow(x) and y <= budget
            elif wantsDanger == "Orange":
                return doSomentingOrange(x) and y <= budget
            else:
                return doSomentingRed(x) and y <= budget

        def IsPymesAllow(x, y, budget, wantsPymes):
            return wantsPymes in x and y <= budget

        numbers = []
        with open("data.json") as f:
            data = json.load(f)
            for item in data:
                if item["type"] == "House":
                    house = House()
                    house.zoneDangerous = item["zoneDangerous"]
                    house.address = item["address"]
                    house.price = item["price"]
                    house.contactPhone = item["contact"]
