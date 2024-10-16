import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {EXPIRY_MODULE_DECLARATIONS, ExpiryRoutingModule} from  './Expiry-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ExpiryRoutingModule
  ],
  declarations: EXPIRY_MODULE_DECLARATIONS,
  exports: EXPIRY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ExpiryModule { }