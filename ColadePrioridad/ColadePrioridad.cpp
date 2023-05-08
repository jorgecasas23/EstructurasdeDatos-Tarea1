#include "cola.h"

colaPrioridad::colaPrioridad(){
}

Elemento Cola::front(){
   Elemento ans = l.infoLista(1);
   return ans;
}

void Cola::enqueue(Elemento e){
   l.anxLista(e);
   l.sort();
}

void Cola::deque(){
   l.elimLista(1);
} 

bool Cola::vaciaCola(){
  bool ans;
  if(l.vaciaLista())
     ans = true;
  else
     ans = false;
  return ans;
}