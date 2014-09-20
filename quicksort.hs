import Control.Monad.Trans.Cont

qsort :: Ord a => [a] -> [a]
qsort xs = runCont (qsort' xs) id
    where qsort' [] = return []
          qsort' (x:xs) = do
              ls <- qsort' $ filter (< x) xs
              rs <- qsort' $ filter (>= x) xs
              return (ls ++ [x] ++ rs)
