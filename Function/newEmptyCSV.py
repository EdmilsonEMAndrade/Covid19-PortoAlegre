def newEmptyCSV(self):
  """
  self = um atributo da tabelha já usada.
  Ex. df[['Atributo']]
  return Empty CSV
  """
  nCSV = self
  
  for c in range(len(nCSV)):
    nCSV.drop(c,inplace=True)
  
  nCSV.drop(columns= self,axis = 1,inplace = True)
  return nCSV
