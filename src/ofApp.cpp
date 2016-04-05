#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    
    
    string path = "/Users/dsak/Desktop/dukeOutdoorAds/images/consolidated/";
    ofDirectory dir(path);
    
    dir.listDir();
    
    finder.setup("haarcascade_frontalface_default.xml");
    finder.setNeighbors(25);
    finder.setScaleHaar(1.05);
    
    //go through and print out all the paths
    for(int i = 0; i < dir.size(); i++){
        ofLog(OF_LOG_NOTICE, "processing element " + ofToString(i));
        
        //printf( "element %i is %s\n", i, splitString[i].c_str() );
        img.load(dir.getPath(i));
        
        
        finder.findHaarObjects(img);
        
        for(unsigned int j = 0; j < finder.blobs.size(); j++) {
            ofRectangle cur = finder.blobs[j].boundingRect;
            //ofDrawRectangle(cur.x, cur.y, cur.width, cur.height);
            cropped.cropFrom(img, cur.x, cur.y, cur.width, cur.height);
            //std::stringstream ss;
            //ss << "chkfaces/" << splitString[i].c_str() << "-";
            string newName = dir.getName(i);
            ofStringReplace(newName, ".jpg", "");
            cropped.save("allfaces/" + newName + "-" + to_string(j+1) + ".jpg");
        }
        
        ofLogNotice(dir.getPath(i));
    }
    
    
    /*
    string path = "/Users/dsak/Desktop/dukeOutdoorAds/images/consolidated/";
    buffer = ofBufferFromFile("id_list_unique_titles_with_chks.txt"); // reading into the buffer
    vector<string> splitString = ofSplitString( buffer.getText(), "\n");
    
    // loop through the results
    for(int i=0; i<splitString.size(); i++){
        
        ofLog(OF_LOG_NOTICE, "processing element " + ofToString(i));
        
        //printf( "element %i is %s\n", i, splitString[i].c_str() );
        img.load(path + splitString[i].c_str() + ".jpg");
        finder.setup("haarcascade_frontalface_default.xml");
        finder.setNeighbors(22);
        finder.setScaleHaar(1.05);
        
        finder.findHaarObjects(img);
        
        for(unsigned int j = 0; j < finder.blobs.size(); j++) {
            ofRectangle cur = finder.blobs[j].boundingRect;
            //ofDrawRectangle(cur.x, cur.y, cur.width, cur.height);
            cropped.cropFrom(img, cur.x, cur.y, cur.width, cur.height);
            std::stringstream ss;
            ss << "chkfaces/" << splitString[i].c_str() << "-";
            cropped.save(ss.str() + to_string(j+1) + ".jpg");
        }
    }
     */
    
    ofLog(OF_LOG_NOTICE, "done.");
    ofExit();

    
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    
   
    
    //cropped.draw(0, 0);
    
    //ofNoFill();
    /*
    for(unsigned int i = 0; i < finder.blobs.size(); i++) {
        ofRectangle cur = finder.blobs[i].boundingRect;
        ofDrawRectangle(cur.x, cur.y, cur.width, cur.height);
    }
     */
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
