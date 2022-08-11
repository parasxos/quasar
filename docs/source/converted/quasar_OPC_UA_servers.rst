quasar OPC UA servers
=========

.. raw:: html

	<html>
	  <head>
	    <title>Summary of known quasar-based OPC-UA servers</title>
	    <style>
	    body
	    {
	        font-family: Arial, Helvetica, sans-serif;
	    }
	
	    table {
	        border-width: 10px;
	        border-collapse: collapse;
	    }
	    td, th {
	        border: 1px solid #bbb;
	        padding: 4px;
	    }
	    th
	    {
	        background-color: #4CAF50;
	        color: white;
	        text-align: left;
	        padding-top: 12px;
	        padding-bottom: 12px;
	    }
	    #tr:nth-child(even){
	    #    background-color: #f2f2f2;
	    #}
	    .tr_phase
	    {
	        background-color: #bce3be;
	        text-align: center;
	        font-style: italic;
	    }
	    </style>
	    <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
	  </head>
	  <p>
	    <i>Generated on 2021-12-08 10:35:02.238736</i>
	    <p>The table is sortable (click on headers!)</p>
	  </p>
	  <table class="sortable">
	    <thead>
	      <tr>
	        <th>Server name</th>
	        <th>quasar version</th>
	        <th>optional modules (non-exhaustive)</th>
	        <th>dflt endpoint</th>
	        <th>#class</th>
	        <th>#cachevariable</th>
	        <th>#sourcevariable</th>
	        <th>#configentry</th>
	        <th>#method</th>
	        <th>#array</th>
	        <th>#object</th>
	        <th>#documentation</th>
	      </tr>
	    </thead>
	    <tr class="tr_phase">
	      <td colspan="100%">Development phase: Production</td>
	    </tr>
	    <tr>
	      <td>JCOP_CAEN</td>
	      <td>1.4.1
	</td>
	      <td>
	        <ul>
	          <li>CommonUtilities (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>4901</td>
	      <td>10</td>
	      <td>20</td>
	      <td></td>
	      <td>12</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>5</td>
	    </tr>
	    <tr>
	      <td>JCOP_ISEG</td>
	      <td>1.4.1
	</td>
	      <td>
	        <ul>
	          <li>CommonUtilities (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>4891</td>
	      <td>9</td>
	      <td>9</td>
	      <td></td>
	      <td>14</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>9</td>
	    </tr>
	    <tr>
	      <td>JCOP_Wiener</td>
	      <td>1.4.1
	</td>
	      <td>
	        <ul>
	          <li>CommonUtilities (ver: master, build-time module)</li>
	          <li>MirrorVariable (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>24911</td>
	      <td>8</td>
	      <td>4</td>
	      <td></td>
	      <td>12</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>5</td>
	    </tr>
	    <tr>
	      <td>JCOP_VENUS_Pilot</td>
	      <td>v1.5.7</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>&lt;b&gt;ERROR&lt;/b&gt;</td>
	      <td>2</td>
	      <td>28</td>
	      <td></td>
	      <td>4</td>
	      <td></td>
	      <td>9</td>
	      <td></td>
	      <td>32</td>
	    </tr>
	    <tr>
	      <td>JCOP_LXI</td>
	      <td>v1.5.1</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>6</td>
	      <td>52</td>
	      <td></td>
	      <td>6</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>1</td>
	    </tr>
	    <tr>
	      <td>JCOP_CANopen</td>
	      <td>Non-quasar</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>48010</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	    </tr>
	    <tr>
	      <td>ATLAS_ATCA</td>
	      <td>v1.5.7</td>
	      <td>
	        <ul>
	          <li>mule (ver: pre-1.1.0-beta1-9-g33a2bb2, git submodule)</li>
	        </ul>
	      </td>
	      <td>48050</td>
	      <td>16</td>
	      <td>169</td>
	      <td>11</td>
	      <td>15</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>2</td>
	    </tr>
	    <tr>
	      <td>ATLAS_SCA</td>
	      <td>Non-quasar</td>
	      <td>
	        <ul>
	          <li>ScaSoftware (ver: 1.5.1-dev1-21-gf36421e, git submodule)</li>
	        </ul>
	      </td>
	      <td>48020</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	      <td>?</td>
	    </tr>
	    <tr>
	      <td>ATLAS_Wiener</td>
	      <td>v1.5.1</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>23401</td>
	      <td>8</td>
	      <td>63</td>
	      <td></td>
	      <td>9</td>
	      <td></td>
	      <td></td>
	      <td>1</td>
	      <td>6</td>
	    </tr>
	    <tr>
	      <td>ATLAS_LArPurity</td>
	      <td>1.3.4
	</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4851</td>
	      <td>3</td>
	      <td>25</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_LArLtdbPerip</td>
	      <td>v1.5.4</td>
	      <td>
	        <ul>
	          <li>UaoClientForOpcUaSca (ver: Error: Repository not found at UaoClientForOpcUaSca, git submodule)</li>
	          <li>UaoForQuasar (ver: for-quasar-1.4.2-8-gadd5e5f, git submodule)</li>
	          <li>cacophony (ver: Error: Repository not found at cacophony, git submodule)</li>
	        </ul>
	      </td>
	      <td>48030</td>
	      <td>14</td>
	      <td>167</td>
	      <td>31</td>
	      <td>21</td>
	      <td>61</td>
	      <td>5</td>
	      <td></td>
	      <td>15</td>
	    </tr>
	    <tr>
	      <td>ATLAS_TileHvMicro</td>
	      <td>1.4.2
	</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4871</td>
	      <td>5</td>
	      <td>105</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_HvSys</td>
	      <td>v1.5.3-rc0</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4891</td>
	      <td>6</td>
	      <td>41</td>
	      <td>6</td>
	      <td>14</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>11</td>
	    </tr>
	    <tr>
	      <td>ATLAS_tRex</td>
	      <td>v1.5.5-rc0</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.8, build-time module)</li>
	          <li>Poverty (ver: v1.0.0, git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>12</td>
	      <td>79</td>
	      <td></td>
	      <td>1</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_reliance</td>
	      <td>v1.5.0</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.6, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>1</td>
	      <td>13</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>14</td>
	    </tr>
	    <tr class="tr_phase">
	      <td colspan="100%">Development phase: Development</td>
	    </tr>
	    <tr>
	      <td>JCOP_PDU</td>
	      <td>v1.5.1</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.10-rc0, build-time module)</li>
	          <li>tools/pdutest/LogIt (ver: Error: Repository not found at tools/pdutest/LogIt, git submodule)</li>
	          <li>tools/pdutest/Mule (ver: Error: Repository not found at tools/pdutest/Mule, git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>8</td>
	      <td>9</td>
	      <td></td>
	      <td>13</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>JCOP_Eltek</td>
	      <td>v1.5.6</td>
	      <td>
	        <ul>
	          <li>CommonUtilities (ver: master, build-time module)</li>
	          <li>mule (ver: #OPCUA-2532-throw-exception-from-openSession-in-event-of-failure, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>5</td>
	      <td>4</td>
	      <td></td>
	      <td>4</td>
	      <td></td>
	      <td></td>
	      <td>2</td>
	      <td>6</td>
	    </tr>
	    <tr>
	      <td>ATLAS_eFex</td>
	      <td>v1.5.3-rc0</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.6-rc0, build-time module)</li>
	          <li>Poverty (ver: up_to_quasar_1.3.x-23-g444c52c, git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>8</td>
	      <td>15</td>
	      <td></td>
	      <td>1</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_gFex</td>
	      <td>1.3.4
	</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.1.2, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>8</td>
	      <td>13</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_itk_rd53a</td>
	      <td>1.4.0
	</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4841</td>
	      <td>2</td>
	      <td>21</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_MOPS</td>
	      <td>1.3.14-rc0
	</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>9</td>
	      <td>15</td>
	      <td></td>
	      <td>6</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_AMAC</td>
	      <td>1.3.11
	</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.2.0, build-time module)</li>
	          <li>Cacophony (ver: Error: Repository not found at Cacophony, git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>3</td>
	      <td>307</td>
	      <td></td>
	      <td>1</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_Shepherd</td>
	      <td>v1.5.1</td>
	      <td>
	        <ul>
	          <li>UaoForQuasar (ver: for-quasar-1.4.2-7-g97cff67, git submodule)</li>
	        </ul>
	      </td>
	      <td>48888</td>
	      <td>1</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>2</td>
	      <td>5</td>
	      <td>1</td>
	      <td>8</td>
	    </tr>
	    <tr>
	      <td>EMP_LpGbt</td>
	      <td>v1.5.0-rc2</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.6-rc0, build-time module)</li>
	          <li>LpGbtSw (ver: Error: cannot describe - no reference found, cannot describe anything., git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>5</td>
	      <td>6</td>
	      <td></td>
	      <td>2</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>SNMP</td>
	      <td>1.4.0
	</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4841</td>
	      <td>3</td>
	      <td>2</td>
	      <td>2</td>
	      <td>5</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_AgilentLab</td>
	      <td>v1.5.2</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.8, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>39</td>
	      <td>203</td>
	      <td></td>
	      <td>26</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>93</td>
	    </tr>
	    <tr>
	      <td>DUNE_WIB</td>
	      <td>v1.5.4</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.10, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>4</td>
	      <td>95</td>
	      <td></td>
	      <td>1</td>
	      <td>5</td>
	      <td></td>
	      <td></td>
	      <td>104</td>
	    </tr>
	    <tr>
	      <td>ATLAS_LAr_SRTM</td>
	      <td>v1.5.0</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: v1.3.6, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>1</td>
	      <td>2</td>
	      <td></td>
	      <td>1</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr class="tr_phase">
	      <td colspan="100%">Development phase: Historic projects (retired, deprecated, cancelled)</td>
	    </tr>
	    <tr>
	      <td>ATLAS_IPBus</td>
	      <td>1.3.4
	</td>
	      <td>
	        <ul>
	          <li>PyEmbed (ver: v1.0.0, build-time module)</li>
	        </ul>
	      </td>
	      <td>4843</td>
	      <td>4</td>
	      <td>22</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>20</td>
	    </tr>
	    <tr>
	      <td>ATLAS_FtkSbc</td>
	      <td>1.3.4
	</td>
	      <td>
	        <ul></ul>
	      </td>
	      <td>4841</td>
	      <td>2</td>
	      <td>45</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>ATLAS_FOS</td>
	      <td>1.3.4
	</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: master, build-time module)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>3</td>
	      <td>1</td>
	      <td></td>
	      <td>3</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td></td>
	    </tr>
	    <tr>
	      <td>TE-CRG</td>
	      <td>1.2.2
	</td>
	      <td>
	        <ul>
	          <li>open62541-compat (ver: master, build-time module)</li>
	          <li>open62541-compat (ver: Error: Repository not found at open62541-compat, git submodule)</li>
	        </ul>
	      </td>
	      <td>4841</td>
	      <td>6</td>
	      <td>22</td>
	      <td></td>
	      <td></td>
	      <td></td>
	      <td>3</td>
	      <td></td>
	      <td>3</td>
	    </tr>
	  </table>
	</html>
