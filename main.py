# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import torchvision
import coremltools as ct
from fastpunct import FastPunct

def test():
    torch_model = torchvision.models.mobilenet_v2(pretrained=True)
    # Set the model in evaluation mode
    # torch_model.eval()


    # example_input = torch.rand(1, 3, 224, 224)  # after test, will get 'size mismatch' error message with size 256x256
    # traced_model = torch.jit.trace(torch_model, example_input)
    fastpunct = FastPunct()
    traced_model = fastpunct.model
    traced_model.save('aaa.h5')
    # Convert to Core ML using the Unified Conversion API
    model = ct.convert(
        traced_model,
        'pytorch',
        inputs=[ct.ImageType(name="input_1", shape=example_input.shape)] # provide only if step 2 was performed
    )

    # Save model
    model.save("MobileNetV2.mlmodel")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
    # fastpunct = FastPunct()
    # result = fastpunct.punct([
    #     "john smiths dog is creating a ruccus",
    #     "ys jagan is the chief minister of andhra pradesh",
    #     "we visted new york last year in may"
    # ])
    # print(result)
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
