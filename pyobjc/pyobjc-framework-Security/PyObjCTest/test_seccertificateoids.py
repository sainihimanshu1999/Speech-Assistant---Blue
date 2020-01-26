from PyObjCTools.TestSupport import *

import Security


class TestSecCertificateOIDs(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecOIDADC_CERT_POLICY, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_CERT_POLICY, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_CODE_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_CODE_SIGNING_DEV, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_ICHAT_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_RESOURCE_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_SYSTEM_IDENTITY, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION, unicode)
        self.assertIsInstance(
            Security.kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING, unicode
        )
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_APPLE_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_CODE_SIGNING, unicode)
        self.assertIsInstance(Security.kSecOIDAuthorityInfoAccess, unicode)
        self.assertIsInstance(Security.kSecOIDAuthorityKeyIdentifier, unicode)
        self.assertIsInstance(Security.kSecOIDBasicConstraints, unicode)
        self.assertIsInstance(Security.kSecOIDBiometricInfo, unicode)
        self.assertIsInstance(Security.kSecOIDCSSMKeyStruct, unicode)
        self.assertIsInstance(Security.kSecOIDCertIssuer, unicode)
        self.assertIsInstance(Security.kSecOIDCertificatePolicies, unicode)
        self.assertIsInstance(Security.kSecOIDClientAuth, unicode)
        self.assertIsInstance(Security.kSecOIDCollectiveStateProvinceName, unicode)
        self.assertIsInstance(Security.kSecOIDCollectiveStreetAddress, unicode)
        self.assertIsInstance(Security.kSecOIDCommonName, unicode)
        self.assertIsInstance(Security.kSecOIDCountryName, unicode)
        self.assertIsInstance(Security.kSecOIDCrlDistributionPoints, unicode)
        self.assertIsInstance(Security.kSecOIDCrlNumber, unicode)
        self.assertIsInstance(Security.kSecOIDCrlReason, unicode)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT, unicode)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EMAIL_SIGN, unicode)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EXTENSION, unicode)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_IDENTITY, unicode)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_POLICY, unicode)
        self.assertIsInstance(Security.kSecOIDDeltaCrlIndicator, unicode)
        self.assertIsInstance(Security.kSecOIDDescription, unicode)
        self.assertIsInstance(Security.kSecOIDEKU_IPSec, unicode)
        self.assertIsInstance(Security.kSecOIDEmailAddress, unicode)
        self.assertIsInstance(Security.kSecOIDEmailProtection, unicode)
        self.assertIsInstance(Security.kSecOIDExtendedKeyUsage, unicode)
        self.assertIsInstance(Security.kSecOIDExtendedKeyUsageAny, unicode)
        self.assertIsInstance(Security.kSecOIDExtendedUseCodeSigning, unicode)
        self.assertIsInstance(Security.kSecOIDGivenName, unicode)
        self.assertIsInstance(Security.kSecOIDHoldInstructionCode, unicode)
        self.assertIsInstance(Security.kSecOIDInvalidityDate, unicode)
        self.assertIsInstance(Security.kSecOIDIssuerAltName, unicode)
        self.assertIsInstance(Security.kSecOIDIssuingDistributionPoint, unicode)
        self.assertIsInstance(Security.kSecOIDIssuingDistributionPoints, unicode)
        self.assertIsInstance(Security.kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH, unicode)
        self.assertIsInstance(Security.kSecOIDKERBv5_PKINIT_KP_KDC, unicode)
        self.assertIsInstance(Security.kSecOIDKeyUsage, unicode)
        self.assertIsInstance(Security.kSecOIDLocalityName, unicode)
        self.assertIsInstance(Security.kSecOIDMS_NTPrincipalName, unicode)
        self.assertIsInstance(Security.kSecOIDMicrosoftSGC, unicode)
        self.assertIsInstance(Security.kSecOIDNameConstraints, unicode)
        self.assertIsInstance(Security.kSecOIDNetscapeCertSequence, unicode)
        self.assertIsInstance(Security.kSecOIDNetscapeCertType, unicode)
        self.assertIsInstance(Security.kSecOIDNetscapeSGC, unicode)
        self.assertIsInstance(Security.kSecOIDOCSPSigning, unicode)
        self.assertIsInstance(Security.kSecOIDOrganizationName, unicode)
        self.assertIsInstance(Security.kSecOIDOrganizationalUnitName, unicode)
        self.assertIsInstance(Security.kSecOIDPolicyConstraints, unicode)
        self.assertIsInstance(Security.kSecOIDPolicyMappings, unicode)
        self.assertIsInstance(Security.kSecOIDPrivateKeyUsagePeriod, unicode)
        self.assertIsInstance(Security.kSecOIDQC_Statements, unicode)
        self.assertIsInstance(Security.kSecOIDSerialNumber, unicode)
        self.assertIsInstance(Security.kSecOIDServerAuth, unicode)
        self.assertIsInstance(Security.kSecOIDStateProvinceName, unicode)
        self.assertIsInstance(Security.kSecOIDStreetAddress, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectAltName, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectDirectoryAttributes, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectEmailAddress, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectInfoAccess, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectKeyIdentifier, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectPicture, unicode)
        self.assertIsInstance(Security.kSecOIDSubjectSignatureBitmap, unicode)
        self.assertIsInstance(Security.kSecOIDSurname, unicode)
        self.assertIsInstance(Security.kSecOIDTimeStamping, unicode)
        self.assertIsInstance(Security.kSecOIDTitle, unicode)
        self.assertIsInstance(Security.kSecOIDUseExemptions, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1CertificateIssuerUniqueId, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1CertificateSubjectUniqueId, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerName, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameCStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameLDAP, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameStd, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SerialNumber, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1Signature, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureAlgorithm, unicode)
        self.assertIsInstance(
            Security.kSecOIDX509V1SignatureAlgorithmParameters, unicode
        )
        self.assertIsInstance(Security.kSecOIDX509V1SignatureAlgorithmTBS, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureCStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectName, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameCStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameLDAP, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameStd, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKey, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKeyAlgorithm, unicode)
        self.assertIsInstance(
            Security.kSecOIDX509V1SubjectPublicKeyAlgorithmParameters, unicode
        )
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKeyCStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1ValidityNotAfter, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1ValidityNotBefore, unicode)
        self.assertIsInstance(Security.kSecOIDX509V1Version, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3Certificate, unicode, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateCStruct, unicode)
        self.assertIsInstance(
            Security.kSecOIDX509V3CertificateExtensionCStruct, unicode
        )
        self.assertIsInstance(
            Security.kSecOIDX509V3CertificateExtensionCritical, unicode
        )
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionId, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionStruct, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionType, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionValue, unicode)
        self.assertIsInstance(
            Security.kSecOIDX509V3CertificateExtensionsCStruct, unicode
        )
        self.assertIsInstance(
            Security.kSecOIDX509V3CertificateExtensionsStruct, unicode
        )
        self.assertIsInstance(
            Security.kSecOIDX509V3CertificateNumberOfExtensions, unicode
        )
        self.assertIsInstance(Security.kSecOIDX509V3SignedCertificate, unicode)
        self.assertIsInstance(Security.kSecOIDX509V3SignedCertificateCStruct, unicode)

    @expectedFailure
    @min_os_level("10.7")
    def test_constants_missing(self):
        self.assertIsInstance(
            Security.kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER, unicode
        )
        self.assertIsInstance(
            Security.kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE, unicode
        )
        self.assertIsInstance(
            Security.kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE, unicode
        )
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE, unicode)
        self.assertIsInstance(
            Security.kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE, unicode
        )

    @min_os_level("10.8")
    def test_constants_10_8(self):
        self.assertIsInstance(Security.kSecOIDSRVName, unicode)


if __name__ == "__main__":
    main()
