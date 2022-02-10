from pathlib import Path
filein_dir = Path('./in')
fileout_dir = Path('./out')

def solve(inp, out):
    num_of_clients = int(inp.readline())
    like_factor = {}
    for i in range(num_of_clients):
        likes = inp.readline().strip().split()
        dislikes = inp.readline().strip().split()

        for ing in likes[1: ]:
            if ing in like_factor:
                like_factor[ing] += 1
            else:
                like_factor[ing] = 1
        
        for ing in dislikes[1: ]:
            if ing in like_factor:
                like_factor[ing] -= 1
            else:
                like_factor[ing] = -1
        
    new_list = [ing for ing in like_factor.keys() if like_factor[ing] > 0]
    
    out.write(f"{len(new_list)}")
    for ing in new_list:
        out.write(f" {ing}")


if __name__ == '__main__':
    input_files = ['a_an_example.in.txt', 'b_basic.in.txt', 'c_coarse.in.txt', 'd_difficult.in.txt', 'e_elaborate.in.txt']

    for input_file_name in input_files:
        filein = filein_dir / input_file_name
        fileout = fileout_dir / f"{input_file_name[:2]}out.txt"

        with open(filein, 'r') as inp, open(fileout, 'w') as out:
            solve(inp, out)
