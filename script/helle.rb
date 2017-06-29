#Ruby 之 HelloWorld  
  
#版本1  
def say_hello1(name)  
  return "Hello , "+ name    
end  
  
#版本2  
def say_hello2 name  
  return "Hello , " + name  
end  
  
#版本3  
def say_hello3 name  
  return "Hello , #{name}"  
end  
  
puts say_hello1 "lql1"  
puts say_hello2 "lql2"  
puts say_hello3 "lql3" 

class Hello

    attr_reader :msg

    def initialize

        @msg = "Hello, World"

    end

end

h = Hello.new

puts h.msg

print "Press RETURN"