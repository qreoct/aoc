import enum
from collections import defaultdict
from typing import List

class Computer:
  def __init__(self):
    self.spaces = [] # sorted [(idx), ...] 
    self.data = defaultdict(list)   # file_id: [(idx), ...]
    self.size = 0
    self.file_id = 0
    pass
  
  ### External methods
  def add_space(self, space_size: int) -> None:
    for i in range(space_size):
      self.spaces.append(i + self.size)
    self.size += space_size
    
  def add_data(self, data_size: int) -> None:
    for i in range(data_size):
      self.data[self.file_id].append(i + self.size)
    self.size += data_size
    self.file_id += 1
    
  def is_sorted(self) -> bool:
    res = min(self.spaces) > max([max(v) for v in self.data.values()])
    # print(f"Is sorted: {res}, because min of spaces {min(self.spaces)} > max of data {max([max(v) for v in self.data.values()])})")
    return res
  
  def shift_right_data_to_space(self):
    """Part 1"""
    # get max idx of data and file_id
    max_data_idx = max([max(v) for v in self.data.values()])
    # get file_id of max data idx
    max_data_file_id = [k for k, v in self.data.items() if max_data_idx in v][0]
    # min idx of space
    min_space_idx = min(self.spaces)
    # shift data to space
    self.data[max_data_file_id].remove(max_data_idx)
    self.data[max_data_file_id].append(min_space_idx)
    self.spaces.remove(min_space_idx)
    self.spaces.append(max_data_idx)
  
    
  def calc_checksum(self) -> int:
    checksum = 0
    for k, v in self.data.items():
      for position in v:
        checksum += k * position
    return checksum
    
  ### Debug methods
  def present(self) -> str:
    for i in range(self.size):
      if i in self.spaces:
        print(".", end="")
      else:
        data_idxs = [k for k, v in self.data.items() if i in v]
        print(f"[{data_idxs[0]}]", end="")
    print('\n')


### Inputs
def read_input(filename: str):
  with open(filename) as f:
    return f.read()
  
def process_input(input: str, comp: Computer):
  
  class Mode(enum.Enum):
    DATA = 1
    SPACE = 2

  curr_mode = Mode.DATA
  
  for idx, ch in enumerate(input):
    if curr_mode == Mode.DATA:
      comp.add_data(int(ch))
      curr_mode = Mode.SPACE
    elif curr_mode == Mode.SPACE:
      comp.add_space(int(ch))
      curr_mode = Mode.DATA

      
    

### Main loop
def main(input: str):
  comp = Computer()
  
  process_input(input, comp)
  # comp.present()
  
  ### PART 1
  rounds = 0
  while not comp.is_sorted():
    comp.shift_right_data_to_space()
    rounds += 1
    if rounds % 100 == 0:
      print(f"Round {rounds}")
    comp.present()
    
  cs = comp.calc_checksum()
  print(cs)

  
  

input = read_input("../in/09a.txt")
main(input)