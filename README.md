This is the start of a turn-based combat game inspired by the game Dungeons and Dragons. To run it you first start Docker, then you create the image using the command below



docker build -t game .



Then you run it with



docker run -it game



The -it flag is important since the program is interactive using the command line 

