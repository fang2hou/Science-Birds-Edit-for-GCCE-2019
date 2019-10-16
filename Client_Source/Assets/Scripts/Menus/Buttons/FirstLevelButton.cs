using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class FirstLevelButton : MonoBehaviour
{
    public int levelID;

    // Start is called before the first frame update
    void Start()
    {      
		// Load levels in the resources folder
		TextAsset []levelsData = Resources.LoadAll<TextAsset>(ABConstants.DEFAULT_LEVELS_FOLDER);

		string[] resourcesXml = new string[levelsData.Length];
		for (int i = 0; i < levelsData.Length; i++)
			resourcesXml [i] = levelsData[i].text;


#if UNITY_WEBGL && !UNITY_EDITOR

		// WebGL builds does not load local files
		string[] streamingXml = new string[0];

#else
		// Load levels in the streaming folder
		string   levelsPath = Application.dataPath + ABConstants.CUSTOM_LEVELS_FOLDER;
		string[] levelFiles = Directory.GetFiles (levelsPath, "*.xml");

		string[] streamingXml = new string[levelFiles.Length];
		for (int i = 0; i < levelFiles.Length; i++)
			streamingXml [i] = File.ReadAllText (levelFiles [i]);

#endif

		// Combine the two sources of levels

		// GCCE DEMO
		// string[] allXmlFiles = new string[resourcesXml.Length + streamingXml.Length];
		string[] allXmlFiles = new string[streamingXml.Length];
		// resourcesXml.CopyTo(allXmlFiles, 0);
		// streamingXml.CopyTo(allXmlFiles, resourcesXml.Length);
		streamingXml.CopyTo(allXmlFiles, 0);
		LevelList.Instance.LoadLevelsFromSource (allXmlFiles);
    }

    public void LoadLevel()
    {        
		ABSceneManager.Instance.LoadScene("GameWorld", true, onSceneLoaded);
    }

    void onSceneLoaded()
    {
		LevelList.Instance.CurrentIndex = levelID;
    }
}
