from datetime import date
from typing import Dict, List, Union


class RentalData(Dict):
    rental_name: str 
    id: int 
    checkin: date 
    checkout: date 
    previous_reservation_id: Union[int, None] 


RentalTableTyping = List[RentalData]