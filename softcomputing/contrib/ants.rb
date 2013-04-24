#!/usr/bin/env ruby
require "csv"

# CONFIGURATION
iterations = 500
numofants = 15
$alpha = 0.4
$rho=0.2

# READ FROM CSV
$magazzini = Array.new
CSV.open("magazzini.csv",{:headers=>:first_row}) do |csv|
  csv.each {|row| $magazzini[csv.lineno-2]=Integer(row['cap'])}
end

$clienti = Array.new
CSV.open("clienti.csv",{:headers=>:first_row}) do |csv|
  csv.each {|row| $clienti[csv.lineno-2]=Integer(row['req'])}
end

$distances = Hash.new
CSV.foreach("distanze.csv",{:headers=>:first_row}) do |row|
  $distances[[Integer(row['Mid'])-1,Integer(row['Cid'])-1]]=Integer(row['dist'])
end

# INITIALIZATION
dmax = $distances.max {|a, b| a[1]<=>b[1]}[1]
tau0 = 2*dmax

$tau = Hash.new
$eta = Hash.new
$distances.each do |key, val|
  $eta[key] = dmax - val
  $tau[key] = tau0
end

# UTILITY FUNCTIONS
def cost(ant)
  cost = 0
  ant.each.with_index do |m, c|
    cost += $distances[[m,c]]
  end
  cost
end

def choose(v)
  selection = rand*v.inject(:+)
  buzz = 0
  v.each.with_index do |value, index| 
    buzz += value
    return index if buzz > selection
  end
end


def findSol
  rc = Array.new
  v = Array.new
  ant = Array.new
  $magazzini.each.with_index {|m, mid| rc[mid] = m }
  $clienti.each.with_index do |c, cid|
    $magazzini.each.with_index do |m, mid|
      v[mid] = rc[mid]>=c ? $alpha*$eta[[mid,cid]]+(1-$alpha)*$tau[[mid,cid]]:0
    end
    ant[cid]=choose(v)
    rc[ant[cid]] -= c
  end
  ant
end

def updateTau
  $clienti.each.with_index do |c, cid|
    $magazzini.each.with_index do |m, mid|
      $tau[[mid,cid]]*=$rho
    end
  end
  zworst = cost $ants.max{|a,b| cost(a)<=>cost(b)}
  $ants.each.with_index do |ant, aid|
    $clienti.each.with_index do |c, cid|
      $tau[[ant[cid],cid]] += zworst - cost(ant)
    end
  end
end


# ANT SEARCH - MAIN LOOP
$ants = Array.new
$bestAnt = Array.new

iterations.times do
  numofants.times do 
    $ants << ant = findSol
    $bestAnt = ant if $bestAnt==[] || cost(ant) < cost($bestAnt)
  end
  updateTau
  $ants.clear
end

p 'Best Ant'
p $bestAnt
counter = Hash.new
$bestAnt.each {|m| counter[m] = (counter[m].nil?)? 1 : counter[m] += 1}
p 'Magazzini'
p counter.sort
p 'Magazzini ordinati per utilizzo'
p counter.sort {|a,b| b[1] <=> a[1]}
p 'Best fitness'
p cost($bestAnt)