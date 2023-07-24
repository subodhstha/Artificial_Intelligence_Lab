/* kheer contains suger
 jeripuri contains suger
 namkeen contains salt
 samosa contains salt
 sweetdish is the dish which contains suger
 saltydish is the dish which contains salt

 logical operation
 validate kheer is sweetdish
 list out saltydish
*/
contains(kheer,suger).
contains(jeripuri,suger).
contains(namkeen,salt).
contains(samosa,salt).
sweetdish(X):-contains(X,suger).
saltydish(X):-contains(X,salt).

/* sweetdish(X) */