import Control.Monad.Trans.Cont
import System.Random

qsort :: Ord a => [a] -> [a]
qsort xs = runCont (qsort' xs) id
    where qsort' [] = return []
          qsort' (x:xs) = do
              ls <- qsort' $ filter (< x) xs
              rs <- qsort' $ filter (>= x) xs
              return (ls ++ [x] ++ rs)

main = do
    ls <- mapM (\x -> randomRIO (0, 100)) [1..100] :: IO [Int]
    print $ qsort ls
