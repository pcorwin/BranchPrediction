from inspect import currentframe, getframeinfo
import matplotlib.pyplot as plt

class BP:
  def __init__(self):
    # initialize whatever you need here
    self.num_checks = 0
    self.num_hits = 0
    self.type = str(input("s for static\n1 for one-bit\n2 for two-bit\n3 for three bit\n"))
    self.keys = {}
    self.predictors = {}
    self.percents = {}

  def check(self, expr):
    frameinfo = getframeinfo(currentframe().f_back)
    this_function = frameinfo.function
    this_line = frameinfo.lineno
    key = this_function + str(this_line)

    if not self.keys.__contains__(key):
      self.num_checks += 1
      self.keys[key] = [0, 0]
      totals = self.keys[key]
      print(f"{key} : total = {totals[1]}; %correct {totals[0] * 100:2.2f}")
      if self.type == "1":
        self.predictors[key] = "1"
      elif self.type == "2":
        self.predictors[key] = "00"
      elif self.type == "3":
        self.predictors[key] = "111"
    else:
      self.num_checks += 1
      totals = self.keys[key]
      totals[1] += 1

      # STATIC
      if self.type == "s":
        if expr == True:
          totals[0] += 1
          self.num_hits += 1

      # ONE-BIT
      elif self.type == "1":
        if self.predictors[key] == "1" and expr == True:
          totals[0] += 1
          self.num_hits += 1
          self.predictors[key] = "1"
        elif  self.predictors[key] == "0" and expr == False:
          totals[0] += 1
          self.num_hits += 1
          self.predictors[key] = "1"
        else:
            self.predictors[key] = "0"

      # TWO-BIT
      elif self.type == "2":
        if expr == True:
            totals[0] += 1
            self.num_hits += 1
            if self.predictors[key] == ("11" or "10"):
                self.predictors[key] = "11"
            elif self.predictors[key] == ("01"):
                self.predictors[key] = "10"
            elif self.predictors[key] == ("00"):
                self.predictors[key] = "10"
        else:
            if self.predictors[key] == ("00" or "01"):
                self.predictors[key] = "00"
            elif self.predictors[key] == ("11"):
                self.predictors[key] = "10"
            elif self.predictors[key] == ("10"):
                self.predictors[key] = "01"


      elif self.type == "3":
        if expr == False:
            if self.predictors[key] == "111":
                self.predictors[key] = "110"
            elif self.predictors[key] == "110":
                self.predictors[key] = "101"
            elif self.predictors[key] == "101":
                self.predictors[key] = "100"
            elif self.predictors[key] == "100":
                self.predictors[key] = "011"
            elif self.predictors[key] == "011":
                self.predictors[key] = "010"
            elif self.predictors[key] == "010":
                self.predictors[key] = "001"
            elif self.predictors[key] == ("000" or "001"):
                self.predictors[key] = "000"
        else:
            totals[0] += 1
            self.num_hits += 1
            if self.predictors[key] == ("111" or "110"):
                self.predictors[key] = "111"
            elif self.predictors[key] == "101":
                self.predictors[key] = "110"
            elif self.predictors[key] == "100":
                self.predictors[key] = "101"
            elif self.predictors[key] == "011":
                self.predictors[key] = "100"
            elif self.predictors[key] == "010":
                self.predictors[key] = "011"
            elif self.predictors[key] == "001":
                self.predictors[key] = "010"
            elif self.predictors[key] == "000":
                self.predictors[key] = "001"

      self.keys[key] = totals
      self.percents[key] = totals[0]/totals[1] * 100
      print(f"{key} : total = {totals[1]}; %correct = {totals[0]/totals[1] * 100:2.2f}")

  def print_summary(self):
    print(f"overall total = {self.num_checks}; %correct = {(self.num_hits / self.num_checks) * 100:2.2f}")
    plt.bar(range(len(self.percents)), list(self.percents.values()), align='center')
    plt.xticks(range(len(self.percents)), list(self.percents.keys()), rotation=75)
    plt.show()

bp_info = BP()
