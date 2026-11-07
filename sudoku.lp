% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% each cell gets exactly one number (1..9)
{ sudoku(X, Y, N) : N = 1..9 } = 1 :- X = 1..9, Y = 1..9.

% initial is part of the answer if initial(X, Y, N) for row X in column Y
sudoku(X, Y, N) :- initial(X, Y, N).

% constraint -- values may not share the same row
:- sudoku(X, Y1, N), sudoku(X, Y2, N), Y1 != Y2.

% constraint -- values may not share the same column
:- sudoku(X1, Y, N), sudoku(X2, Y, N), X1 != X2.

% the subgrid with the formula for G that cell (X, Y) belongs to
subgrid(X, Y, G) :-
    X = 1..9,
    Y = 1..9,
    G = 1 + (((X-1)/3)*3 + (Y-1)/3).

% constraint -- there can be no repeated number in a subgrid
:- sudoku(X1, Y1, N),
   sudoku(X2, Y2, N),
   subgrid(X1, Y1, G),
   subgrid(X2, Y2, G),
   X1 != X2,
   Y1 != Y2.

#show sudoku/3.
