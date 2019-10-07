var fibonacci = function(n) 
{
  if(n==1) 
  {
    return [0, 1];
  } 
  else 
  {
    var m = fibonacci(n - 1);
    m.push(m[m.length - 1] + m[m.length - 2]);
    return m;
  }
};

 console.log(fibonacci(10));
