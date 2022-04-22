class Frequency:
    def execution(self):
        self.Sstring = "Hello World"
        self.my_list = {}
  
        for i in self.Sstring:
            if i in self.my_list:
                self.my_list[i] += 1
            else:
                self.my_list[i] = 1
  
        return "Count of all characters in Hello World is :\n " +  str(self.my_list)

test = Frequency()
result = test.execution()
print(result)