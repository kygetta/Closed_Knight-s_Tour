#COSC 420 - Project 2
The Closed Knight’s Tour

About: 
	The Knight’s Tour is a chess problem that first appeared hundreds of years ago. It has a simple goal: using the Knight, move to every space on a chess board (or any NxN board) without ever jumping to the same position twice.  The solution is not quite as simple as the goal.  You will need to utilize multiprocessing in order to find all of the closed tour solutions as efficiently as possible. A Closed Knight’s Tour is one that is described as having the Knight visit every space on the board ONLY ONCE while ending up just ONE Knight move (L-shaped move) away from the origin.

Assignment:
<details><summary>Step 1:</summary>
<p>
	<li>Create a Python program to find all possible paths for a Closed Knight’s Tour on any given N x N chess board.</li>
	<li>We will be using even numbers only for N as Closed Tours are only possible with an even number of squares</li>
	<li>Use the Depth First Search (DFS) algorithm</li>
	<li>Your program should accept command line arguments for N and the starting position of the knight as X and Y</li>
	<li>Example. python solve_knights_tour.py 6 1 3</li>
	<li>command line args:</li>
		N = 6
		X = 1
		Y = 3
	<li>Print out the total execution time at the end of the program</li>
	<li>Create another process that's sole purpose is to create a file that stores all solved solutions.</li>
	<li>This means you will have to use IPC to pass a solution from one of your algorithm process to this file writing process in order to save the data</li>
	<li>These solutions should be an NxN grid depicting where the Knight moved</li>
	<li>The origin should mark move 0 and the final position should mark move NxN</li>
	<li>For example, on a 5x5 board there will be 25 positions.  The origin will be marked 0 and the final position will be marked 24.</li>
	<li>All moves should be stored as a NxN matrix</li>
	<li>Cap the number of saved solutions at 100,000.</li>
<p>
</details>
