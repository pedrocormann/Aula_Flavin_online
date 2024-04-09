/**
 * (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.
 */

//==============================================================================
// Welcome to scripting in Meta Spark Studio! Helpful links:
//
// Scripting Basics - https://fb.me/spark-scripting-basics
// Reactive Programming - https://fb.me/spark-reactive-programming
// Scripting Object Reference - https://fb.me/spark-scripting-reference
// Changelogs - https://fb.me/spark-changelog
//
// Meta Spark Studio extension for VS Code - https://fb.me/spark-vscode-plugin
//
// For projects created with v87 onwards, JavaScript is always executed in strict mode.
//==============================================================================

// How to load in modules
// Load in the required modules
const Reactive = require('Reactive');
const Animation = require('Animation');
const Scene = require('Scene');

// Use export keyword to make a symbol available in scripting debug console
export const Diagnostics = require('Diagnostics');

// To use variables and functions across files, use export/import keyword
// export const animationDuration = 10;

// Use import keyword to import a symbol from another file
// import { animationDuration } from './script.js'

async function asyncCall() {  // Enables async/await in JS [part 1]

  // To access scene objects
  // const [directionalLight] = await Promise.all([
  //   Scene.root.findFirst('directionalLight0')
  // ]);

  // To access class properties
  // const directionalLightIntensity = directionalLight.intensity;

  // To log messages to the console
  // Diagnostics.log('Console message logged from the script.');

  try {
    // To access scene objects
    const [emitter] = await Promise.all([
      Scene.root.findFirst('emitter')
    ]);
    Diagnostics.log("emitter found");
    Diagnostics.log("Emitter");
    if (emitter != null) {
      Diagnostics.log("emmiter != null");
      emitter.birthrate = 200;
      emitter.birthrateDelta = 0.5;


      //const sizeSampler = Animation.samplers.linear(0.002,0.001);
      //emitter.sizeModifier = sizeSampler;

      // Create polybezier samplers for X,Y and Z values with arbitrary values for keyframes
      const samplerX = Animation.samplers.polybezier({keyframes:[0,0.11,0,-0.01,0],knots:[0,1,2,3,4]})
      const samplerY = Animation.samplers.polybezier({keyframes:[-0.01,0,-0.11,0,0.11],knots:[0,1,2,3,4]})
      const samplerZ = Animation.samplers.polybezier({keyframes:[-0.05,0.05,-0.05,0.05,-0.05],knots:[0,1,2,3,4]})

      // Use XYZ samplers to modify position of particles over time
      emitter.positionModifier = [samplerX,samplerY,samplerZ];

    } else {
      Diagnostics.log("emmiter == null");
    }

  } catch (e) {
    Diagnostics.log(e);
  }
}

asyncCall(); // Enables async/await in JS [part 2]

