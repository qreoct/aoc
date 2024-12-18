import enum
from collections import defaultdict
from typing import List

class Computer:
  def __init__(self):
    self.spaces = defaultdict(list) # size_of_space: [(idx), ...]
    self.data = defaultdict(list)   # file_id: [(idx), ...]
    self.size = 0
    self.file_id = 0
    pass
  
  ### External methods
  def add_space(self, space_size: int) -> None:
    self.spaces[space_size].append(self.size)
    self.size += space_size
    
  def add_data(self, data_size: int) -> None:
    for i in range(data_size):
      self.data[self.file_id].append(i + self.size)
    self.size += data_size
    self.file_id += 1
    
  def is_sorted(self) -> bool:
    res = min([s for v in self.spaces.values for s in v]) > max([max(v) for v in self.data.values()])
    # print(f"Is sorted: {res}, because min of spaces {min(self.spaces)} > max of data {max([max(v) for v in self.data.values()])})")
    return res
    
  def shift_right_block_data_to_space(self):
    """Part 2"""
    
    for file_id in sorted(self.data.keys(), reverse=True):
      print(f"File id: {file_id}")
      left_limit_idx = min(self.data[file_id])
      data_size = len(self.data[file_id])
      min_space_idx = None
      
      # starting from data_size to max_space_size, and find the most leftmost smallest value that can take the block
      for space_size_to_look_for in range(data_size, max(self.spaces.keys()) + 1, 1):
        if space_size_to_look_for in self.spaces:
          possible_spaces = list(filter(lambda x: x < left_limit_idx, self.spaces[space_size_to_look_for]))
          if len(possible_spaces) > 0:
            min_space_idx = min(min(possible_spaces), min_space_idx) if min_space_idx else min(possible_spaces)
      
      if min_space_idx:
        # move data
        print(f"moving file id {file_id} of size {data_size} to space {min_space_idx}")
        self.data[file_id] = [min_space_idx + i for i in range(data_size)]
        space_size_to_look_for = next(key for key, value in self.spaces.items() if min_space_idx in value)
        self.spaces[space_size_to_look_for].remove(min_space_idx)
        self.spaces[data_size].append(left_limit_idx)
        self.spaces[data_size].sort()
        
        space_size_diff = space_size_to_look_for - data_size
        if space_size_diff > 0:
          self.spaces[space_size_diff].append(min_space_idx + data_size)
          self.spaces[space_size_diff].sort()
  
    
  def calc_checksum(self) -> int:
    checksum = 0
    for k, v in self.data.items():
      for position in v:
        checksum += k * position
    return checksum
    
  ### Debug methods
  def present(self) -> str:
    for i in range(self.size):
      in_data = any(i in v for v in self.data.values())
      in_spaces = any(i in v for v in self.spaces.values())
      if in_data:
        data_idxs = [k for k, v in self.data.items() if i in v]
        print(f"[{data_idxs[0]}]", end="")
      elif in_spaces:
        k = [k for k, v in self.spaces.items() if i in v]
        print("." * k[0], end="")
        
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
  print("processed input")
  print(f"spaces: {comp.spaces}")
  
  ### PART 1
  # rounds = 0
  # while not comp.is_sorted():
  #   comp.shift_right_data_to_space()
  #   rounds += 1
  #   if rounds % 100 == 0:
  #     print(f"Round {rounds}")
  #   comp.present()
    
  ### PART 2
  space_size = len(comp.spaces)
  comp.shift_right_block_data_to_space()
    
  cs = comp.calc_checksum()
  print(cs)

  
  

input = read_input("../in/09a.txt")
main(input)