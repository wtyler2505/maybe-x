#!/usr/bin/env python3
"""
Backend API Testing Script
Tests all backend endpoints using the production URL from frontend/.env
"""

import requests
import json
import uuid
from datetime import datetime
import os
import sys
from pathlib import Path

def load_base_url():
    """Load the base URL from frontend/.env"""
    frontend_env_path = Path(__file__).parent / "frontend" / ".env"
    
    if not frontend_env_path.exists():
        print(f"❌ Frontend .env file not found at {frontend_env_path}")
        return None
    
    with open(frontend_env_path, 'r') as f:
        for line in f:
            if line.startswith('REACT_APP_BACKEND_URL='):
                base_url = line.split('=', 1)[1].strip()
                print(f"✅ Using base URL: {base_url}")
                return base_url
    
    print("❌ REACT_APP_BACKEND_URL not found in frontend/.env")
    return None

def test_hello_endpoint(base_url):
    """Test GET /api endpoint"""
    print("\n🔍 Testing GET /api endpoint...")
    
    try:
        url = f"{base_url}/api"
        response = requests.get(url, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("message") == "Hello World":
                    print("✅ GET /api - PASSED")
                    return True
                else:
                    print(f"❌ GET /api - FAILED: Expected message 'Hello World', got {data}")
                    return False
            except json.JSONDecodeError:
                print(f"❌ GET /api - FAILED: Invalid JSON response")
                return False
        else:
            print(f"❌ GET /api - FAILED: Expected status 200, got {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ GET /api - FAILED: Request error - {e}")
        return False

def test_health_endpoint(base_url):
    """Test GET /api/health endpoint"""
    print("\n🔍 Testing GET /api/health endpoint...")
    
    try:
        url = f"{base_url}/api/health"
        response = requests.get(url, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("status") == "ok":
                    print("✅ GET /api/health - PASSED")
                    return True
                else:
                    print(f"❌ GET /api/health - FAILED: Expected status 'ok', got {data}")
                    return False
            except json.JSONDecodeError:
                print(f"❌ GET /api/health - FAILED: Invalid JSON response")
                return False
        else:
            print(f"❌ GET /api/health - FAILED: Expected status 200, got {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ GET /api/health - FAILED: Request error - {e}")
        return False

def test_create_status(base_url):
    """Test POST /api/status endpoint"""
    print("\n🔍 Testing POST /api/status endpoint...")
    
    try:
        url = f"{base_url}/api/status"
        payload = {"client_name": "preview_tester"}
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                # Check required fields
                if "id" not in data:
                    print("❌ POST /api/status - FAILED: Missing 'id' field")
                    return False, None
                
                if "client_name" not in data:
                    print("❌ POST /api/status - FAILED: Missing 'client_name' field")
                    return False, None
                
                if "timestamp" not in data:
                    print("❌ POST /api/status - FAILED: Missing 'timestamp' field")
                    return False, None
                
                # Validate UUID format
                try:
                    uuid.UUID(data["id"])
                    print(f"✅ ID is valid UUID: {data['id']}")
                except ValueError:
                    print(f"❌ POST /api/status - FAILED: ID is not a valid UUID: {data['id']}")
                    return False, None
                
                # Validate client_name
                if data["client_name"] != "preview_tester":
                    print(f"❌ POST /api/status - FAILED: Expected client_name 'preview_tester', got {data['client_name']}")
                    return False, None
                
                # Validate timestamp format
                try:
                    datetime.fromisoformat(data["timestamp"].replace('Z', '+00:00'))
                    print(f"✅ Timestamp is valid ISO8601: {data['timestamp']}")
                except ValueError:
                    print(f"❌ POST /api/status - FAILED: Invalid timestamp format: {data['timestamp']}")
                    return False, None
                
                print("✅ POST /api/status - PASSED")
                return True, data
                
            except json.JSONDecodeError:
                print(f"❌ POST /api/status - FAILED: Invalid JSON response")
                return False, None
        else:
            print(f"❌ POST /api/status - FAILED: Expected status 200, got {response.status_code}")
            return False, None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ POST /api/status - FAILED: Request error - {e}")
        return False, None

def test_get_status_list(base_url, created_item=None):
    """Test GET /api/status endpoint"""
    print("\n🔍 Testing GET /api/status endpoint...")
    
    try:
        url = f"{base_url}/api/status"
        response = requests.get(url, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                if not isinstance(data, list):
                    print(f"❌ GET /api/status - FAILED: Expected array, got {type(data)}")
                    return False
                
                print(f"✅ Response is an array with {len(data)} items")
                
                # If we created an item, verify it exists in the list
                if created_item:
                    found_item = None
                    for item in data:
                        if item.get("id") == created_item.get("id"):
                            found_item = item
                            break
                    
                    if found_item:
                        print(f"✅ Created item found in list: {found_item}")
                        
                        # Validate the found item has all required fields
                        required_fields = ["id", "client_name", "timestamp"]
                        for field in required_fields:
                            if field not in found_item:
                                print(f"❌ GET /api/status - FAILED: Missing field '{field}' in list item")
                                return False
                        
                        # Validate UUID format
                        try:
                            uuid.UUID(found_item["id"])
                        except ValueError:
                            print(f"❌ GET /api/status - FAILED: Invalid UUID in list item: {found_item['id']}")
                            return False
                        
                        # Validate timestamp format
                        try:
                            datetime.fromisoformat(found_item["timestamp"].replace('Z', '+00:00'))
                        except ValueError:
                            print(f"❌ GET /api/status - FAILED: Invalid timestamp in list item: {found_item['timestamp']}")
                            return False
                        
                        print("✅ GET /api/status - PASSED")
                        return True
                    else:
                        print(f"❌ GET /api/status - FAILED: Created item not found in list")
                        return False
                else:
                    print("✅ GET /api/status - PASSED (no specific item to verify)")
                    return True
                
            except json.JSONDecodeError:
                print(f"❌ GET /api/status - FAILED: Invalid JSON response")
                return False
        else:
            print(f"❌ GET /api/status - FAILED: Expected status 200, got {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ GET /api/status - FAILED: Request error - {e}")
        return False

def check_cors_headers(base_url):
    """Check CORS headers are present"""
    print("\n🔍 Checking CORS headers...")
    
    try:
        # Test with GET request including Origin header (simulates browser request)
        url = f"{base_url}/api"
        headers = {"Origin": "https://example.com"}
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        cors_headers = {
            'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
            'Access-Control-Allow-Credentials': response.headers.get('Access-Control-Allow-Credentials'),
        }
        
        print(f"CORS Headers: {cors_headers}")
        
        # Check for Access-Control-Allow-Origin header
        if cors_headers['Access-Control-Allow-Origin']:
            print("✅ CORS headers are present")
            return True
        else:
            print("❌ CORS headers not found")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ CORS check - FAILED: Request error - {e}")
        return False

def main():
    """Main test runner"""
    print("🚀 Starting Backend API Tests")
    print("=" * 50)
    
    # Load base URL
    base_url = load_base_url()
    if not base_url:
        print("❌ Cannot proceed without base URL")
        sys.exit(1)
    
    # Track test results
    results = []
    
    # Test 1: GET /api
    results.append(("GET /api", test_hello_endpoint(base_url)))
    
    # Test 2: GET /api/health
    results.append(("GET /api/health", test_health_endpoint(base_url)))
    
    # Test 3: POST /api/status
    create_success, created_item = test_create_status(base_url)
    results.append(("POST /api/status", create_success))
    
    # Test 4: GET /api/status
    results.append(("GET /api/status", test_get_status_list(base_url, created_item)))
    
    # Test 5: CORS headers
    results.append(("CORS headers", check_cors_headers(base_url)))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{test_name}: {status}")
        if success:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("💥 Some tests failed!")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)