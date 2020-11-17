# use vectors to store the string 
# then process the sums of these numbers
# use an if statement to evaluate which is 

even_or_odd <- function(s){
  v <- as.integer(strsplit(s,"")[[1]]) 
  sume <- sum(subset(v, v %% 2 == 0))
  sumo <- sum(subset(v, !v %% 2 == 0))

  if (sume > sumo){
    if{print("Even is greater than Odd")}
  }else if (sumo > sume){
      print("Odd is greater than Even")
  }else{
      print("Even and Odd are the same")
      }
  # alternative case statement commented out as 
  # it does not work with the version of R  
  # that codewars uses
  #case_when(sumo == sume ~ "Even and Odd are the same",
  #         sumo < sume ~ "Even is greater than Odd",
  #         TRUE ~ "Odd is greater than Even")
  

}