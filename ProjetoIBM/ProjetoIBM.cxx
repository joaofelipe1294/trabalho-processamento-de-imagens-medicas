#include <iostream>
#include "FileHandler.hpp"
#include "OptimalThreshold.hpp"
#include "DataCollector.hpp"
#include "KNNClassifier.hpp"
#include "LabelFinder.hpp"

#include "TrainPipeline.hpp"
#include "PreProcessPipeline.hpp"

using namespace std;
using namespace itk;

int main(int argc, char * argv[]){
    string imageName , dirName , input;
    bool needToTrain = NULL;
    if(argc == 2){
        imageName = argv[1];
        needToTrain = false;
    }else if (argc == 3){
        dirName = argv[1];
        imageName = argv[2];
        needToTrain = true;
    }else{
        cout << "Treinar (S/N): ";
        cin >> input;
        if(input.compare("S") == 0 || input.compare("s") == 0){
            needToTrain = true;
            cout << "Pasta de treinamento : ";
            cin >> dirName;
        }else if(input.compare("N") || input.compare("n")){
            needToTrain = false;
        }
        cout << "Imagem a ser classificada : ";
        cin >> imageName;
    }
    
/* -------------------------------------------------- TRAIN ---------------------------------------------- */
 
    if(needToTrain == true){
        TrainPipeline* trainPipeline = new TrainPipeline(dirName);
        trainPipeline -> Train();
    }
    
/* ------------------------------------------------------------------------------------------------------- */

/* ------------------------------------------------- PRE PROCESS ------------------------------------------ */
    
    PreProcessPipeline* preProcess = new PreProcessPipeline(imageName);
    preProcess -> Process();
    
/* --------------------------------------------------------------------------------------------------------- */
    
    return EXIT_SUCCESS;
}