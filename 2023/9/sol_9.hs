main = (print . sum . map (extrapolate2 . map read . words) . lines)
       =<< readFile "input.in"

extrapolate1 :: [Integer] -> Integer
extrapolate1 ls
  | all (== 0) ls = 0
  | otherwise = last ls + extrapolate1 (zipWith (-) (tail ls) ls)

extrapolate2 :: [Integer] -> Integer
extrapolate2 ls
  | all (== 0) ls = 0
  | otherwise = head ls - extrapolate2 (zipWith (-) (tail ls) ls)
