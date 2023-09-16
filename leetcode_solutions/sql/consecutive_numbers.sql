select num as ConsecutiveNums
from (
       select num,
              lag(num, 1) over() as prev,
              lag(num, 2) over() as prev_prev
       from Logs 
) as sub
where num = prev and num = prev_prev
