//
//  Optimalthreshold.hpp
//  ProjetoIBM
//
//  Created by joao lopes on 09/06/16.
//
//

#ifndef Optimalthreshold_hpp
#define Optimalthreshold_hpp

#include <stdio.h>
#include "itkImage.h"

using namespace itk;

typedef Image<unsigned char , 2> GrayscaleImageType;

class Optimalthreshold{
private:
    GrayscaleImageType::Pointer originalImage;
    GrayscaleImageType::Pointer thresholdImage;
public:
    Optimalthreshold(GrayscaleImageType::Pointer);
    int GetOutput();
private:
    void ApplyThreshold(int value , GrayscaleImageType::Pointer original , GrayscaleImageType::Pointer thresholdImage);
};

#endif /* Optimalthreshold_hpp */
