import json
from skimage import io
import click
import os
import hashlib


@click.command()
@click.option('--path', type = click.STRING, required=True, 
        help = 'path to json file on disk')
@click.option('--folder', type = click.STRING, default = 'default_folder', 
        help = 'path to directory, where to save images')
def main(path, folder):
    if not os.path.isfile(path):
        print('there is no file named {}\n exiting...'.format(path))
        return 1
    if not os.path.isdir(folder):
        print('Creating folder {}'.format(folder))
        os.makedirs(folder)
    with open(path, 'r') as f:
        data = json.loads(f.read())
    data_len = len(data)
    print('Got {} images'.format(data_len))
    for i, example in enumerate(data):
        image = io.imread(example['source'])
        hash_name = hashlib.md5(example['source'].encode('utf-8')).hexdigest()
        for j, obj in enumerate(example['objects']):
            print('Processing image {} object {}. {}%'.format(i+1, j+1,
                int(100*(float(i)/data_len))))
            file_name = '{}/{}_{}_{}.jpg'.format(folder, j, i, hash_name)
            if os.path.isfile(file_name):
                print('File {} already exist, skipping'.format(file_name))
                continue
            points = [[int(p['x']),int(p['y'])]
                    for p in obj['polygon']['vertexes']]
            x_min, y_min = map(min, list(zip(*points)))
            x_max, y_max = map(max, list(zip(*points)))
            cut_image = image[y_min:y_max,x_min:x_max]
            io.imsave(file_name, cut_image)
    print('Processing done')
    return 0
if __name__=='__main__':
    main()
