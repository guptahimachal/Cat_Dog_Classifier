
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[ Contributors ][contributors-url]
[ Forks ][forks-url]
[ Stargazers ][stars-url]
[ Issues ][issues-url]
[ LinkedIn ][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/
           /Cat_Dog_Classifier">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Cat_Dog_Classifier</h3>

  <p align="center">
    The following project is a Cat-Dog classifier, implemented using CNN and deployed using tflite as an android application
    <br />
    <a href="https://github.com/guptahimachal/Cat_Dog_Classifier"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/guptahimachal/Cat_Dog_Classifier">View Demo</a>
    ·
    <a href="https://github.com/guptahimachal/Cat_Dog_Classifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/guptahimachal/Cat_Dog_Classifier/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


**Image Classification - Cat or Dog using Convolution Neural Network:**
I have used Google Colab Notebook and implemented with keras



<!-- GETTING STARTED -->
## Getting Started
The datasets are taken from [Kaggle][Dataset]. It consist of 8000 training set and 2000 test set.
I have used the 2000 test images for validation
### Prerequisites

* tensorflow - '1.15.2'
* Keras - '2.2.4-tf'

### Installation


1. For selecting tensorflow in  Colab Notebook
```python
%tensorflow_version 1.x
import tensorflow as tf
```
2. Keras
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
``` 



<!-- USAGE EXAMPLES -->
## Usage

Using this project we can extend it to classification of images to different other classes , For example it can be used in tagging images while storing if one has to store a lot
of images and search among them.
**Directory Structure-**




<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/guptahimachal/Cat_Dog_Classifier/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/guptahimachal/Cat_Dog_Classifier](https://github.com/guptahimachal/Cat_Dog_Classifier)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-url]: https://github.com/guptahimachal/Cat_Dog_Classifier/graphs/contributors
[forks-url]: https://github.com/guptahimachal/Cat_Dog_Classifier/network/members
[stars-url]: https://github.com/guptahimachal/Cat_Dog_Classifier/stargazers
[issues-url]: https://github.com/guptahimachal/Cat_Dog_Classifier/issues
[license-url]: https://github.com/guptahimachal/Cat_Dog_Classifier/blob/master/LICENSE.txt
[linkedin-url]: https://linkedin.com/in/guptahimachal
[product-screenshot]: images/screenshot.png
[Dataset]: https://www.kaggle.com/chetankv/dogs-cats-images
